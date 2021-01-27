"""Classes used to share SSH connections and SSH tunnels.

Since activating an SSH connection usually takes some time, those are 
kept active and shared between the different requests.
"""
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
from typing import Tuple, Dict, Optional, Type, Any, List
from types import TracebackType

resolver = dns.resolver.Resolver()
resolver.nameservers = ["224.0.0.251"]
resolver.port = 5353


def resolve_hostname(hostname: str) -> Tuple[str, bool]:
    """Convert a hostname to ip using dns first and then mdns.

    If it does not resolve it, returns the original value (in
    case this may be parsed in some smarter ways down the line).

    :param hostname: name to be solved
    :type hostname: str
    :returns: tuple with ip address as string and flag telling if mdns has been used
    :rtype: tuple

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
    """Class used to manage a SHH tunnels.

    since creating the tunnel is time consuming, all connections to docker on the device will share the same tunnel

    """

    __tunnels: Dict[str, "SharedSSHDockerTunnel"] = {}
    __lock = threading.RLock()
    sshtunnel.SSHTunnelForwarder.skip_tunnel_checkup = False

    @classmethod
    def get_tunnel(
        cls, device: "targetdevice.TargetDevice"
    ) -> Optional["SharedSSHDockerTunnel"]:
        """Return an SharedSSHDockerTunnel object,allocating it if it's required.

        :param device: destination device
        :tpye device: targetdevice.TargetDevice
        :returns: tunnel object
        :rtype: SharedSSHDockerTunnel

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
        """Connect to the device via SSH tunneling.

        :param device: target device
        :type device: targetdevice.TargetDevice

        """
        logging.info("SSH - Creating tunnel to " + str(device.id))

        self.device_id = device.id
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

    def __enter__(self) -> "SharedSSHDockerTunnel":
        """Lock the object when used in with statement."""
        self.__objlock.acquire()
        return self

    @classmethod
    def remove_tunnel(cls, device_id: str) -> None:
        """Close the connection to a specific device after an error.

        :param device_id: target device id
        :type device: str

        """
        with cls.__lock:
            if device_id in cls.__tunnels:
                logging.info("SSH - Tunnel to " + device_id + " closed")
                connection = cls.__tunnels[device_id]
                del cls.__tunnels[device_id]
                thread = threading.Thread(target=connection.stop)
                thread.start()

    def __exit__(
        self,
        etype: Optional[Type[BaseException]],
        value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> Optional[bool]:
        """Ensure that tunnel is closed when an exception occours during operations."""
        try:
            self.__objlock.release()
        except:
            pass

        try:
            if etype is not None:
                assert self.device_id is not None
                SharedSSHClient.remove_connection(self.device_id)
                SharedSSHDockerTunnel.remove_tunnel(self.device_id)
                self.close()

                logging.info("SSH - Tunnel to " + self.device_id + " closed")
                with SharedSSHDockerTunnel.__lock:
                    if self.device_id in SharedSSHDockerTunnel.__tunnels:
                        del SharedSSHDockerTunnel.__tunnels[self.device_id]
                        thread = threading.Thread(target=self.stop)
                        thread.start()
        except:
            pass

        return None


class IgnorePolicy(paramiko.MissingHostKeyPolicy):
    """Helper class for SSH implementation.

    Policy for automatically adding the hostname and new host key to the
    local `.HostKeys` object, and saving it.  This is used by `.SSHClient`.

    """

    def missing_host_key(self, client: Any, hostname: Any, key: Any) -> None:
        """Handle missing host key (does nothing, justs n ignore thes n reques -> Nonet to save hostname/key pairs).

        :param client:
        :param hostname:
        :param key:

        """
        pass


class SharedSSHClient(paramiko.SSHClient):
    """Class used to manage SSH connection to a specific device.

    Since activating SSH connections is time-consuming, all commands are sent on a shared connection.

    """

    __connections: Dict[str, "SharedSSHClient"] = {}
    __lock = threading.RLock()

    @classmethod
    def get_connection(cls, device: "targetdevice.TargetDevice") -> "SharedSSHClient":
        """Return an SSH connection object,allocating it if it's required.

        :param device: destination device
        :type device: targetdevice.TargetDevice
        :returns: connection object
        :rtype: SharedSSHClient

        """
        with cls.__lock:
            if device.id in cls.__connections:
                ssh = cls.__connections[device.id]

                transport = ssh.get_transport()

                if (
                    transport is not None
                    and transport.is_active()
                    and transport.is_alive()
                ):
                    return ssh
                try:
                    ssh.close()
                except:
                    pass

            k = paramiko.RSAKey.from_private_key(io.StringIO(device.privatekey))

            assert device.id is not None

            ssh = cls(device.id)

            # ssh.load_system_host_keys()
            ssh.set_missing_host_key_policy(IgnorePolicy())

            ip, mdns = resolve_hostname(device.hostname)

            ssh.connect(ip, 22, username=device.username, pkey=k, allow_agent=False)

            logging.info("SSH - Connected to device " + str(device.id))

            cls.__connections[str(device.id)] = ssh
            return ssh

    def __init__(self, device_id: str):
        """Initialize object.

        :param device: device id
        :type device: targetdevice.TargetDevice
        """
        self.device_id = device_id
        self.__objlock = threading.RLock()
        super().__init__()
        logging.info("SSH - Connecting to device " + device_id)

    def __enter__(self) -> "SharedSSHClient":
        """Lock the object when used in with statements."""
        self.__objlock.acquire()
        return self

    @classmethod
    def remove_connection(cls, device_id: str) -> None:
        """Remove a connection after an error.

        :param device_id: ID of the device that needs to be removed from the list
        :type device: targetdevice.TargetDevice

        """
        with cls.__lock:
            if device_id in cls.__connections:
                logging.info("SSH - Connection to " + device_id + " closed")
                del cls.__connections[device_id]

    def __exit__(
        self,
        etype: Optional[Type[BaseException]],
        value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        """Close the connection if an exception is generated during operations."""
        self.__objlock.release()
        if etype is not None:
            SharedSSHClient.remove_connection(self.device_id)
            SharedSSHDockerTunnel.remove_tunnel(self.device_id)
            self.close()


class SSHForwarder(threading.Thread):
    """Class that implements port forwarding via SSH.

    Forwards traffic from a local port to SSH default port on a device in a secure way.

    """

    MAX_BLOCK_SIZE = 65536

    def __init__(
        self,
        listenthread: "SSHListenThread",
        socket: socket.socket,
        device: "targetdevice.TargetDevice",
    ):
        """Create forwarding thread.

        :param listenthread: object that accepted the incoming connection
        :type listenthread: SSHListenThread
        :param socket: socket that has been created during accept
        :type socket: socket.socket
        :param device: target device
        :type device: targetdevice.TargetDevice

        """
        super().__init__()

        self.socket = socket
        self.parent = listenthread
        self.device = device
        self.ssh: Optional[paramiko.SSHClient] = None
        self.stopped = False

    def run(self) -> None:
        """Forward data between the local and remote ports."""
        channel = None

        try:
            k = paramiko.RSAKey.from_private_key(io.StringIO(self.device.privatekey))

            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(IgnorePolicy())

            ip, mdns = resolve_hostname(self.device.hostname)

            self.ssh.connect(
                ip, 22, username=self.device.username, pkey=k, allow_agent=False
            )

            channel = self.ssh.invoke_shell()

            self.socket.setblocking(False)
            channel.setblocking(False)

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
            if channel is not None:
                channel.shutdown(2)
            self.socket.shutdown(socket.SHUT_RDWR)
        except Exception:
            pass

        if not self.stopped:
            self.parent.client_closed(self)

    def stop(self) -> None:
        """Stop traffic forwarding."""
        self.stopped = True
        self.socket.shutdown(socket.SHUT_RDWR)
        self.socket.close()


class SSHListenThread(threading.Thread):
    """Class that creates a forward channel for any connection on local port."""

    def __init__(self, port: Optional[int], device: "targetdevice.TargetDevice"):
        """Initialize socket and start listening for connections.

        :param port: destination port on the target, if port is None, then port number will be assigned by the system
        :type port: int, optional
        :param device: target device
        :type device: targetdevices.TargetDevice

        """
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
        self.clients: List[SSHForwarder] = []

    def get_port(self) -> int:
        """Return used port."""
        assert self.port is not None
        return self.port

    def run(self) -> None:
        """Accept incoming connections and create forward thread."""
        while True:
            client = self.socket.accept()[0]
            forwarder = SSHForwarder(self, client, self.device)
            self.clients.append(forwarder)
            forwarder.start()

    def stop(self) -> None:
        """Stop accepting incoming connections and close all pending forward threads."""
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

    def client_closed(self, client: SSHForwarder) -> None:
        """Remove a client from the active clients list.

        :param client: client to be remove
        :type client: SSHForwarder

        """
        if client in self.clients:
            self.clients.remove(client)
