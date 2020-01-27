import io
import threading
import logging
import paramiko
import sshtunnel
import select


class SharedSSHDockerTunnel(sshtunnel.SSHTunnelForwarder):

    __tunnels = {}
    __lock = threading.RLock()
    sshtunnel.SSHTunnelForwarder.skip_tunnel_checkup = False

    @classmethod
    def get_tunnel(cls, device):
        """
        Returns an SharedSSHDockerTunnel object,
        allocating it if it's required

        Arguments:
            device {TargetDevice} -- device

        Returns:
            SharedSSHDockerTunnel -- object
        """

        with cls.__lock:
            if device.id in cls.__tunnels:
                return cls.__tunnels[device.id]

            tunnel = None

            for _ in range(0, 10):
                try:
                    tunnel = cls(device)
                except sshtunnel.HandlerSSHTunnelForwarderError:
                    continue
                break

            if tunnel is None:
                return None

            cls.__tunnels[device.id] = tunnel
            return tunnel

    def __init__(self, device):

        logging.info("SSH - Creating tunnel to " + device.id)

        self.device = device.id
        self.__objlock = threading.RLock()
        k = paramiko.RSAKey.from_private_key(
            io.StringIO(device.privatekey))

        super().__init__(
            ssh_address_or_host=device.hostname,
            ssh_username=device.username,
            ssh_pkey=k,
            remote_bind_address=("127.0.0.1", 2375))

        # otherwise first connection always fails
        self.start()
        logging.info("SSH - Tunnel to " + device.id + " activated")

    def __enter__(self):
        self.__objlock.acquire()
        return self

    def __exit__(self, type, value, traceback):
        self.__objlock.release()

        if type:
            logging.info("SSH - Tunnel to " + self.device + " closed")
            with SharedSSHDockerTunnel.__lock:
                if self.device in SharedSSHDockerTunnel.__tunnels:
                    del SharedSSHDockerTunnel.__tunnels[self.device]
                    self.stop()


class SharedSSHClient(paramiko.SSHClient):

    __connections = {}
    __lock = threading.RLock()

    @classmethod
    def get_connection(cls, device):
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
                if ssh.get_transport().is_active():
                    return ssh
                try:
                    ssh.close()
                except:
                    pass

            k = paramiko.RSAKey.from_private_key(
                io.StringIO(device.privatekey))

            ssh = cls(device.id)

            ssh.load_system_host_keys()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            ssh.connect(device.hostname,
                        22,
                        username=device.username,
                        pkey=k)

            logging.info("SSH - Connected to device " + device.id)

            cls.__connections[device.id] = ssh
            return ssh

    def __init__(self, device):
        self.device = device
        self.__objlock = threading.RLock()
        super().__init__()
        logging.info("SSH - Connecting to device " + device)

    def __enter__(self):
        self.__objlock.acquire()
        return self

    def __exit__(self, type, value, traceback):
        self.__objlock.release()
        if type:
            with SharedSSHClient.__lock:
                logging.info("SSH - Connection to " + self.device + " closed")
                if self.device in SharedSSHClient.__connections:
                    del SharedSSHClient.__connections[self.device]
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
            k = paramiko.RSAKey.from_private_key(
                io.StringIO(self.device.privatekey))

            self.ssh = paramiko.SSHClient()
            self.ssh.load_system_host_keys()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            self.ssh.connect(self.device.hostname,
                             22,
                             username=self.device.username,
                             pkey=k)

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
            forwarder = SSHForwarder(self,
                                     client,
                                     self.device)
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
