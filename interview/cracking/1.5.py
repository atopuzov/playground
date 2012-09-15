def replaceSpace(s):
    result = ""
    for c in s:
        if c == " ":
            result += "%20"
        else:
            result += c
    return result


s = "This is a sample string"
print s, replaceSpace(s)

