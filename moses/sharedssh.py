import io
import threading
import logging
import paramiko
import sshtunnel
import select
import time
import dns.resolver
import socket
import targetdevice
from typing import Tuple, Dict, Optional

resolver = dns.resolver.Resolver()
resolver.nameservers = ["224.0.0.251"]
resolver.port = 5353


def resolve_hostname(hostname: str) -> Tuple[str, bool]:
    """
    Convert a hostname to ip using dns first and then mdnsself.
    If it does not resolve it, returns the original value (in
    case this may be parsed in some smarter ways down the line)

    Arguments:
        hostname {str} -- mnemonic name

    Returns:
        str -- ip address as string
        bool - true id mdns has been used
    """
    global resolver

    ip = hostname
    mdns = False

    try:
        ip = socket.gethostbyname(hostname)
    except socket.gaierror:
        if not hostname.endswith(".local"):
            hostname += ".local"

        try:
            addr = resolver.query(hostname, "A")

            if addr is not None and len(addr) > 0:
                ip = addr[0].to_text()
                mdns = True
        except:
            pass
    except:
        pass
    return ip, mdns


class SharedSSHDockerTunnel(sshtunnel.SSHTunnelForwarder):

    __tunnels: Dict[str, "SharedSSHDockerTunnel"] = {}
    __lock = threading.RLock()
    sshtunnel.SSHTunnelForwarder.skip_tunnel_checkup = False

    @classmethod
    def get_tunnel(
        cls, device: "targetdevice.TargetDevice"
    ) -> Optional["SharedSSHDockerTunnel"]:
        """
        Returns an SharedSSHDockerTunnel object,
        allocating it if it's required

        Arguments:
            device {TargetDevice} -- device

        Returns:
            SharedSSHDockerTunnel -- object
        """

        with cls.__lock:
            tunnel = None

            if device.id in cls.__tunnels:
                tunnel = cls.__tunnels[device.id]

                if tunnel.is_active and tunnel.is_alive:
                    return tunnel
                else:
                    tunnel = None

            for _ in range(0, 10):
                try:
                    tunnel = cls(device)
                except sshtunnel.HandlerSSHTunnelForwarderError:
                    continue
                break

            if tunnel is None:
                return None

            timeout = 100

            while not (tunnel.is_active and tunnel.is_alive):
                time.sleep(0.1)
                timeout = timeout - 1
                if timeout == 0:
                    return None

            cls.__tunnels[str(device.id)] = tunnel
            return tunnel

    def __init__(self, device: "targetdevice.TargetDevice"):

        logging.info("SSH - Creating tunnel to " + str(device.id))

        self.device = device.id
        self.__objlock = threading.RLock()

        k = paramiko.RSAKey.from_private_key(io.StringIO(device.privatekey))

        ip, mdns = resolve_hostname(device.hostname)

        super().__init__(
            ssh_address_or_host=ip,
            ssh_username=device.username,
            ssh_pkey=k,
            remote_bind_address=("127.0.0.1", 2375),
            allow_agent=False,
        )

        # otherwise first connection always fails
        self.start()
        logging.info("SSH - Tunnel to " + str(device.id) + " activated")

    def __enter__(self):
        self.__objlock.acquire()
        return self

    @classmethod
    def remove_tunnel(cls, device):
        with cls.__lock:
            if device in cls.__tunnels:
                logging.info("SSH - Tunnel to " + device + " closed")
                connection = cls.__tunnels[device]
                del cls.__tunnels[device]
                thread = threading.Thread(target=connection.stop)
                thread.start()

    def __exit__(self, type, value, traceback):
        try:
            self.__objlock.release()
        except:
            pass

        try:
            if type:
                SharedSSHClient.remove_connection(self.device)
                SharedSSHDockerTunnel.remove_tunnel(self.device)
                self.close()

                logging.info("SSH - Tunnel to " + self.device + " closed")
                with SharedSSHDockerTunnel.__lock:
                    if self.device in SharedSSHDockerTunnel.__tunnels:
                        del SharedSSHDockerTunnel.__tunnels[self.device]
                        thread = threading.Thread(target=self.stop)
                        thread.start()
        except:
            pass


class IgnorePolicy(paramiko.MissingHostKeyPolicy):
    """
    Policy for automatically adding the hostname and new host key to the
    local `.HostKeys` object, and saving it.  This is used by `.SSHClient`.
    """

    def missing_host_key(self, client, hostname, key):
        pass


class SharedSSHClient(paramiko.SSHClient):

    __connections: Dict[str, "SharedSSHClient"] = {}
    __lock = threading.RLock()

    @classmethod
    def get_connection(cls, device: "targetdevice.TargetDevice") -> "SharedSSHClient":
        """
        Returns an SSH connection object,
        allocating it if it's required

        Arguments:
            device {TargetDevice} -- device

        Returns:
            SharedSSHClient -- object
        """

        with cls.__lock:
            if device.id in cls.__connections:
                ssh = cls.__connections[device.id]
                if (
                    ssh.get_transport() is not None
                    and ssh.get_transport().is_active()
                    and ssh.get_transport().is_alive()
                ):
                    return ssh
                try:
                    ssh.close()
                except:
                    pass

            k = paramiko.RSAKey.from_private_key(io.StringIO(device.privatekey))

            ssh = cls(device.id)

            # ssh.load_system_host_keys()
            ssh.set_missing_host_key_policy(IgnorePolicy())

            ip, mdns = resolve_hostname(device.hostname)

            ssh.connect(ip, 22, username=device.username, pkey=k, allow_agent=False)

            logging.info("SSH - Connected to device " + str(device.id))

            cls.__connections[str(device.id)] = ssh
            return ssh

    def __init__(self, device):
        self.device = device
        self.__objlock = threading.RLock()
        super().__init__()
        logging.info("SSH - Connecting to device " + device)

    def __enter__(self):
        self.__objlock.acquire()
        return self

    @classmethod
    def remove_connection(cls, device):
        with cls.__lock:
            if device in cls.__connections:
                logging.info("SSH - Connection to " + device + " closed")
                del cls.__connections[device]

    def __exit__(self, type, value, traceback):
        self.__objlock.release()
        if type:
            SharedSSHClient.remove_connection(self.device)
            SharedSSHDockerTunnel.remove_tunnel(self.device)
            self.close()


class SSHForwarder(threading.Thread):

    MAX_BLOCK_SIZE = 65536

    def __init__(self, listenthread, socket, device):
        super().__init__()

        self.socket = socket
        self.parent = listenthread
        self.device = device
        self.ssh = None
        self.stopped = False

    def run(self):

        try:
            k = paramiko.RSAKey.from_private_key(io.StringIO(self.device.privatekey))

            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(IgnorePolicy())

            ip, mdns = resolve_hostname(self.device.hostname)

            self.ssh.connect(
                ip, 22, username=self.device.username, pkey=k, allow_agent=False
            )

            channel = self.ssh.invoke_shell()

            self.socket.setblocking(0)
            channel.setblocking(0)

            inputs = [self.socket, channel]

            while True:
                ready = select.select(inputs, [], [], None)

                for r in ready[0]:

                    if r == self.socket:
                        data = self.socket.recv(self.MAX_BLOCK_SIZE)
                        channel.send(data)

                    if r == channel:
                        data = channel.recv(self.MAX_BLOCK_SIZE)
                        self.socket.send(data)

        except paramiko.SSHException:
            if not self.stopped:
                pass
        except Exception:
            if not self.stopped:
                pass

        try:
            channel.shutdown(2)
            self.socket.shutdown(socket.SHUT_RDWR)
        except Exception:
            pass

        if not self.stopped:
            self.parent.client_closed(self)

    def stop(self):
        self.stopped = True
        self.socket.shutdown(socket.SHUT_RDWR)
        self.socket.close()


class SSHListenThread(threading.Thread):
    def __init__(self, port, device):
        super().__init__()

        self.device = device
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if port is not None and port != 0:
            self.socket.bind(("127.0.0.1", port))
        else:
            self.socket.bind(("127.0.0.1", 0))
            port = self.socket.getsockname()[1]

        self.port = port
        self.socket.listen(5)
        self.clients = []

    def get_port(self) -> int:
        return self.port

    def run(self):

        while True:
            client = self.socket.accept()[0]
            forwarder = SSHForwarder(self, client, self.device)
            self.clients.append(forwarder)
            forwarder.start()

    def stop(self):

        try:
            self.socket.shutdown(socket.SHUT_RDWR)
            self.socket.close()
        except Exception:
            pass

        for client in self.clients:
            try:
                client.stop()
            except Exception:
                pass

    def client_closed(self, client):

        if client in self.clients:
            self.clients.remove(client)
