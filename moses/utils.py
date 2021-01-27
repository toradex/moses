"""Utility functions."""
import re
from typing import Generator, Optional, Any, Callable


def _replace_tag(
    match: re.Match, tagfn: Callable[[str, str, Any], str], args: Any
) -> str:
    """Replace a tag with the corresponding value.

    :param match:
    :type match: re.Match
    :param tagfn: function used to convert tag to value
    :type tagfn: Callable[[str, str, Any], str]
    :returns: value of the tag
    :rtype: str

    """
    tagstr = str(match.group(0))[2:-2]

    if "." in tagstr:
        obj, tag = tagstr.split(".")[0:2]

        if tag is None or obj is None:
            return tagstr

        obj = obj.lower()
        tag = tag.lower()

        tagstr = tagfn(obj, tag, args)

    return tagstr


tag = re.compile("#%.*?%#")


def replace_tags(text: str, tagfn: Callable[[str, str, Any], str], args: Any) -> str:
    """Replace tags marked with #%<tag>%# in the source string.

    :param text: source string
    :type text: str
    :param tagfn: callback used to resolve tags
    :type tagfn: Callable[[str, str, Any], str]
    :param args: arguments passed to the callback
    :type args: Any
    :returns: string with tags replaced
    :rtype: str

    """
    global tag

    newtext = text

    while "#%" and "%#" in newtext:
        newtext = re.sub(tag, lambda m: _replace_tag(m, tagfn, args), newtext)

    return newtext


def apply_template(
    templatepath: str, outputpath: str, tagfn: Callable[[str, str, Any], str], args: Any
) -> None:
    """Replace tags in the template file to generate the output file.

    :param templatepath: path of the template file
    :type templatepath: str
    :param outputpath: path of the generated file
    :type outputpath: str
    :param tagfn: callback used to resolve tags
    :type tagfn: Callable[[str, str, Any], str]
    :param args: arguments passed to the callback
    :type args: Any

    """
    # processes template replacing #%XXX%# escapes
    # with corresponding fields
    with open(str(templatepath), "r") as inp:
        with open(str(outputpath), "w", newline="\n") as out:
            for _, line in enumerate(inp):
                newline = replace_tags(line, tagfn, args)
                out.write(newline)


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

        for b in log:
            c = b.decode("utf-8")
            line += c
            emptylog = False
            if "\n" in line:
                break

        if emptylog:
            return None

        return line

    except StopIteration:
        return line if not emptylog else None
