"""Functions used to convert the output of command line tools into a json-friendly format."""
from typing import List, Dict, Any, Iterable


def process_ps_output(stream: Iterable[str]) -> List[Dict[str, Any]]:
    """Convert output of ps command into a jsonizable dictionary.

    :param stream: output of ps command
    :type stream: Iterable[str]

    :returns: list of running processes with their properties as dictionary
    :rtype: List[Dict[str,Any]]

    """
    # 1st row contains headers
    first = True
    processes = []

    for line in stream:
        if first:
            first = False
            continue
        fields = line.split()

        if len(fields) < 7:
            continue

        process: Dict[str, Any] = {}
        process["pid"] = int(fields[0])
        process["ppid"] = int(fields[1])
        process["user"] = str(fields[2])
        process["time"] = str(fields[3])
        process["nice"] = 0 if str(fields[4]) == "-" else int(fields[4])
        process["state"] = str(fields[5])
        cmd = str(fields[6])

        for i in range(7, len(fields)):
            cmd = cmd + " " + str(fields[i])

        process["args"] = cmd
        processes.append(process)

    return processes


def process_free_output(stream: Iterable[str]) -> Dict[str, int]:
    """Collect output of free command as jsonizable dictionary.

    :param stream: output of free command
    :type stream: Iterable[str]

    :returns: MemInfo struct (total/free/available kb) as property dictionary
    :rtype: Dict[str, int]

    """
    # 1st row contains headers
    first = True

    meminfo = {"total": -1, "free": -1, "available": -1}

    for line in stream:
        if first:
            first = False
            continue

        fields = line.split()

        meminfo["total"] = int(fields[1])
        meminfo["free"] = int(fields[3])
        meminfo["available"] = int(fields[6])

        # only 1st line needs to be parsed
        break

    return meminfo


def process_df_output(stream: Iterable[str]) -> List[Dict[str, Any]]:
    """Collect output of df command as a list of jsonable dictionary.

    :param stream: output of df command
    :type stream: Iterable[str]

    :returns: StorageInfo struct as property dictionary
    :rtype: List[Dict[str,Any]]

    """
    # 1st row contains headers
    first = True
    storages = []

    for line in stream:
        if first:
            first = False
            continue

        fields = line.split()

        if len(fields) < 6:
            continue

        storage: Dict[str, Any] = {}
        storage["filesystem"] = fields[0]
        storage["size"] = int(fields[1])
        storage["available"] = int(fields[3])
        storage["mountpoint"] = fields[5]

        storages.append(storage)

    return storages
