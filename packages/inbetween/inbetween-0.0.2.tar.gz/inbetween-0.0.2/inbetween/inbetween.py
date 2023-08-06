import re


def inbetween(
    filecontent=None,
    after_array=None,
    before_string=None,
    command="before",
    text=None,
):

    pivots = []
    pivots.extend(after_array)
    pivots.append(before_string)
    count = 0
    isexecuted = False
    deletebetween = False
    result = []
    for line in filecontent:
        wrte = True
        if count <= len(pivots) - 1:
            regexsearch = re.match(pivots[count], line)
            if regexsearch:
                count += 1
                if (
                    count == len(pivots) - 1
                    and command == "deletebetween"
                ):
                    deletebetween = True
                if not isexecuted and count == len(pivots):
                    isexecuted = False
                    wrte = False
                    if command == "delete":
                        continue
                    if command == "deletebetween":
                        deletebetween = False
                    if command == "writebefore":
                        result.append(text)
                    if command == "writeup":
                        result.append(text + "\n")
                    if line[-1] == "\n":
                        line = line[:-1]
                    result.append(line)
                    if command == "writeafter":
                        result.append(text)
                    if command == "writedown":
                        result.append("\n" + text)

        if wrte and not deletebetween:
            result.append(line)
    return result
