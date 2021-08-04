"""Modules that uses mdns to solve device names.

Using regular DNS don't work on many networks and configuring
the IP may be problematic on network that don't have static IPs.
mDNS provides a good solution for small LANs and does not require
a server or router configuration.

"""

from typing import Tuple
import socket
import dns.resolver

resolver = dns.resolver.Resolver()
resolver.nameservers = ["224.0.0.251"]
resolver.port = 5353


# resolver is global to avoid re-initialization at every call
# pylint: disable = global-statement
# pylint: disable = invalid-name
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

    ipaddress = hostname
    mdns = False

    # pylint: disable = broad-except
    try:
        info = socket.getaddrinfo(hostname, 0, 0, 0, 0)

        for addrinfo in info:
            if addrinfo[0] == socket.AF_INET:
                # if not empty we got our address
                if addrinfo[4][0]:
                    ipaddress = addrinfo[4][0]
                    break

    except socket.gaierror:
        if not hostname.endswith(".local"):
            hostname += ".local"

        try:
            addr = resolver.query(hostname, "A")

            if addr is not None and len(addr) > 0:
                ipaddress = addr[0].to_text()
                mdns = True
        except Exception:
            pass
    except Exception:
        pass

    return ipaddress, mdns
