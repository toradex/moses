"""Functions used to use tags and teplates.

This is used to convert platform templates into actual dockerfiles and to
expand tags into property values.
"""
import re
from typing import Any, Callable

TAG = re.compile("#%.*?%#")


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


# regular expression does not change and having
# it as global gives a performance improvment
# pylint: disable = global-statement
def replace_tags(text: str, tagfn: Callable[[
                 str, str, Any], str], args: Any) -> str:
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
    global TAG

    newtext = text

    while "#%" and "%#" in newtext:
        newtext = re.sub(TAG, lambda m: _replace_tag(m, tagfn, args), newtext)

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
