"""Manages proxies to safely access shared a docker registry."""
import logging
import os
import platform
import socket
import sys
import tempfile
from typing import Optional,IO
import docker
import config
import targetdevice
import singleton
import sharedssh
import remotedocker
import nameresolution

# pylint: disable = too-few-public-methods
class DockerProxy( metaclass=singleton.Singleton):
    """Manages local docker registry used to deploy containers to the devices."""

    def __init__(self) -> None:
        """Check if proxy is already running, otherwise start it."""
        if config.ServerConfig().registry is None:
            logging.error("Fatal error. Can't start proxy if no valid registry is configured.")
            sys.exit(-1)

        registry = config.ServerConfig().registry
        assert registry is not None

        if ":" in registry:
            address = registry.split(":")[:2]
            self._hostname = address[0]
            self._port = int(address[1])
        else:
            self._hostname = registry
            self._port = 443

        self._certpath=config.ServerConfig().certspath / (self._hostname+".cert")
        self._containername = self._hostname+"_TIE_docker_proxy"
        self._conffile : Optional[IO[str]] = None

        if not os.path.exists(self._certpath):
            logging.error(f"Fatal error. Can't find certificate {self._certpath}.")
            sys.exit(-1)

        self.localurl = self._hostname+":"+str(self._port)

        config.ServerConfig().registry = self.localurl
        logging.info(f"Docker registry configured as {self.localurl}.")

    def __del__(self) -> None:
        """Clean up temporary file."""
        if self._conffile is not None:
            os.unlink(self._conffile.name)

    def _get_configuration_file(self) -> str:

        return f"""
            upstream docker {{
                server        {self._hostname}:{self._port};
            }}

            server {{
                listen        80;
                server_name   localhost;

                location / {{
                    proxy_pass  https://docker;
                }}
            }}

            access_log stderr;
            error_log stderr info;
            """

    def _start_container(self) -> docker.models.containers.Container:
        docker_client = docker.from_env()

        registryip,_=nameresolution.resolve_hostname(self._hostname)

        if platform.system() == "Windows":
            tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcp.bind(('', 0))
            _, port = tcp.getsockname()
            tcp.close()
        else:
            port = None

        self._conffile = tempfile.NamedTemporaryFile(mode="w", delete=False)

        self._conffile.write(self._get_configuration_file())
        self._conffile.close()

        container = docker_client.containers.run("nginx:alpine",
            name = self._containername,
            ports = {
                "80/tcp" : port
                },
            volumes = {
            self._conffile.name : {
                    "bind" : "/etc/nginx/conf.d/default.conf",
                    "mode" : "rw"
                },
            config.ServerConfig().certspath : {
                    "bind" : "/etc/ssl/private",
                    "mode" : "rw"
                }
            },
            extra_hosts = {
                self._hostname : registryip
            },
            detach = True)

        while container.status == "created":
            container = docker_client.containers.get(self._containername)

        if container.status != "running":
            logging.error("Fatal error. Can't start proxy container.")
            sys.exit(-1)
        return container

    def setup_client(self, device: targetdevice.TargetDevice) -> int:
        """Enable a client device to connect to the registry.

        :param device: device
        :type device: targetdevice.TargetDevice
        """
        assert self._hostname is not None
        assert self._containername is not None
        assert self._certpath is not None

        ipcmd = f"nslookup {self._hostname} | awk '/^Address 1: / {{ A=$3 }}; END {{ print A }}'"

        with remotedocker.RemoteDocker(device) as remote_docker:

            container = remote_docker.get_container(self._containername)

            if container is not None:
                # pylint: disable = broad-except
                try:
                    container.stop()
                    container.remove(force=True)
                except Exception:
                    pass

            with sharedssh.SharedSSHClient.get_connection(device) as ssh:
                _,stdout,_ = ssh.exec_command(ipcmd)
                registryip=stdout.read().decode("UTF-8").strip()
                ssh.exec_command(f"mkdir -p {device.homefolder}/certs")
                certspath=device.homefolder+"/certs"
                confpath=device.homefolder+"/"+self._hostname+".conf"
                conffile=f"""
                    upstream docker {{
                        server        {self._hostname}:{self._port};
                    }}

                server {{
                    listen        80;
                    server_name   nginx.reverse.tie;

                    location / {{
                        proxy_pass  https://docker;
                    }}
                }}"""

                ssh.exec_command(f"echo '{conffile}' > {confpath}")

                sftp = ssh.open_sftp()

                assert sftp is not None

                sftp.put(str(self._certpath),certspath+"/"+self._hostname+".cert")
                sftp.close()

                container = remote_docker.remotedocker.containers.run(
                    "nginx:alpine",
                    name = self._containername,
                    ports = {
                        "80/tcp" : None
                        },
                    volumes = {
                    confpath : {
                            "bind" : "/etc/nginx/conf.d/default.conf",
                            "mode" : "rw"
                        },
                    certspath : {
                            "bind" : "/etc/ssl/private",
                            "mode" : "rw"
                        }
                    },
                    extra_hosts = {
                        self._hostname : registryip
                    },
                    remove = True,
                    detach = True
                )

            while container.status == "created":
                container = remote_docker.get_container(self._containername)

            if container.status != "running":
                return -1

        return container.ports["80/tcp"][0]["HostPort"]
