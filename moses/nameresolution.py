"""Modules that uses mdns to solve device names.

Using regular DNS don't work on many networks and configuring
the IP may be problematic on network that don't have static IPs.
mDNS provides a good solution for small LANs and does not require
a server or router configuration.

"""
import socket
import dns.resolver
from typing import Tuple

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
