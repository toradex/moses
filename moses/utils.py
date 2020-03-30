import re


def _replace_tag(match, tagfn, args) -> str:
    """Replaces a tag with the corresponding value

    Arguments:
        match {re.Match} -- match object
        tagfn -- function used to convert tag to value
        args -- additional arguments passed to tagfn

    Return:

        str -- value of the tag
    """
    tagstr = str(match.group(0))[2:-2]

    if '.' in tagstr:
        obj, tag = tagstr.split('.')

        if tag is None or obj is None:
            return tagstr

        obj = obj.lower()
        tag = tag.lower()

        tagstr = tagfn(obj, tag, args)

    return tagstr


tag = re.compile("#%.*?%#")


def replace_tags(text: str, tagfn, args) -> str:

    global tag

    newtext = text

    while "#%" and "%#" in newtext:
        newtext = re.sub(tag,
                         lambda m:
                         _replace_tag(m, tagfn, args),
                         newtext)

    return newtext


def apply_template(templatepath: str, outputpath: str, tagfn, args):
    """Replaces tags in the template file to generate output file

    Arguments:
        templatepath {str} -- template path
        outputpath {str} -- output file path
        tagfn -- function used to convert tag to value
        args -- additional arguments passed to tagfn
    """
    # processes template replacing #%XXX%# escapes
    # with corresponding fields
    with open(str(templatepath), "r") as inp:
        with open(str(outputpath), "w", newline="\n") as out:
            for _, line in enumerate(inp):
                newline = replace_tags(line, tagfn, args)
                out.write(newline)
