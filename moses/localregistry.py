"""Manages a local docker registry running on the developer's PC."""
import logging
import os
import platform
import socket
import sys
import OpenSSL
import docker
import config
import targetdevice
import singleton
import sharedssh
import remotedocker

# pylint: disable = too-few-public-methods
class LocalRegistry(metaclass=singleton.Singleton):
    """Manages local docker registry used to deploy containers to the devices."""

    def __init__(self) -> None:
        """Check if registry is already running, otherwise start it."""
        self._hostname = socket.gethostname()+".tie"
        self._containername = socket.gethostname()+"_TIE_docker_registry"
        self._keypath=config.ServerConfig().certspath / (self._hostname+".key")
        self._certpath=config.ServerConfig().certspath / (self._hostname+".cert")

        # check if container is already running
        docker_client = docker.from_env()

        container = None

        try:
            container = docker_client.containers.get(self._containername)
        except docker.errors.NotFound:
            pass

        if container is not None:
            if container.status != "running":
                # pylint: disable = broad-except
                try:
                    container.stop()
                    container.remove(force=True)
                except Exception:
                    pass

                container = None
            else:
                self._port = container.ports["5000/tcp"][0]["HostPort"]

        if container is None:
            self._generate_certificate()
            container = self._start_container()

        self.localurl = "localhost:"+self._port

        config.ServerConfig().registry = self.localurl
        logging.info(f"Local docker registry {self._containername} running on {self.localurl}.")

    def _generate_certificate(self) -> None:

        if os.path.exists(self._keypath) and os.path.exists(self._certpath):
            return

        k = OpenSSL.crypto.PKey()
        k.generate_key(OpenSSL.crypto.TYPE_RSA, 4096)

        cert = OpenSSL.crypto.X509()
        cert.get_subject().C = "CH"
        cert.get_subject().ST = "LU"
        cert.get_subject().L = "Horw"
        cert.get_subject().O = "Toradex AG"
        cert.get_subject().OU = "Torizon"
        cert.get_subject().CN = self._hostname
        cert.get_subject().emailAddress = "torizoncore@toradex.com"
        cert.set_serial_number(0)
        cert.gmtime_adj_notBefore(0)
        cert.gmtime_adj_notAfter(10*365*24*60*60)
        cert.set_issuer(cert.get_subject())
        cert.set_pubkey(k)
        cert.sign(k, 'sha512')

        with open(self._certpath, "wt") as certfile:
            certfile.write(
                OpenSSL.crypto.dump_certificate(
                    OpenSSL.crypto.FILETYPE_PEM, cert).decode("utf-8"))
        with open(self._keypath, "wt") as keyfile:
            keyfile.write(
                OpenSSL.crypto.dump_privatekey(
                    OpenSSL.crypto.FILETYPE_PEM, k).decode("utf-8"))

    def setup_client(self, device: targetdevice.TargetDevice) -> int:
        """Enable a client device to connect to the registry.

        :param device: device
        :type device: targetdevice.TargetDevice
        """
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
                _,stdout,_=ssh.exec_command("echo $SSH_CLIENT | awk '{print $1}'")
                localip=stdout.read().decode("UTF-8").strip()
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
                        self._hostname : localip
                    },
                    remove = True,
                    detach = True
                )

            while container.status == "created":
                container = remote_docker.get_container(self._containername)

            if container.status != "running":
                return -1

        return container.ports["80/tcp"][0]["HostPort"]

    def _start_container(self) -> docker.models.containers.Container:
        volumename = socket.gethostname()+"_TIE_docker_registry"


        docker_client = docker.from_env()

        try:
            docker_client.volumes.get(volumename)
        except docker.errors.NotFound:
            docker_client.volumes.create(volumename)

        if platform.system() == "Windows":
            tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcp.bind(('', 0))
            _, port = tcp.getsockname()
            tcp.close()
        else:
            port = None

        container = docker_client.containers.run("registry:2",
            name = self._containername,
            ports = {
                "5000/tcp" : port
                },
            volumes = {
            volumename : {
                    "bind" : "/var/lib/registry",
                    "mode" : "rw"
                },
                config.ServerConfig().certspath : {
                    "bind" : "/certs",
                    "mode" : "rw"
                }
            },
            environment = {
            "REGISTRY_HTTP_ADDR" :
                "0.0.0.0:5000",
            "REGISTRY_HTTP_TLS_CERTIFICATE" :
                "/certs/"+self._hostname+".cert",
            "REGISTRY_HTTP_TLS_KEY" :
                "/certs/"+self._hostname+".key"
            },
            remove = True,
            detach = True)

        while container.status == "created":
            container = docker_client.containers.get(self._containername)

        if container.status != "running":
            logging.error("Fatal error. Can't start local registry container.")
            sys.exit(-1)

        self._port = container.ports["5000/tcp"][0]["HostPort"]
        return container
