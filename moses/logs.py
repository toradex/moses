"""Functions used to manage containers logs.

Since user can access logs from device or application objects shared code
will be in this module.
"""
from typing import Generator, Optional


def get_log_chunk(log: Generator) -> Optional[str]:
    """Return a chunk from the log, avoiding single bytes (from interactive containers).

    :param log: generator
    :type log: generator
    :returns: log chunk or None
    :rtype: str

    """
    line = ""
    emptylog = True

    try:

        for logbyte in log:
            logchar = logbyte.decode("utf-8")
            line += logchar
            emptylog = False
            if "\n" in line:
                break

        if emptylog:
            return None

        return line

    except StopIteration:
        return line if not emptylog else None
