def is_palindrome_iterative(string):
    for i in xrange(len(string)):
        if string[i] != string[-(i+1)]:
            return False
    return True

def is_palindrome_recursive(string):
    if len(string) == 0:
        return True
    elif len(string) == 1:
        return True
    else:
        return string[0] == string[-1] and \
            is_palindrome_recursive(string[1:-1])

a = "anavolimilovana"
print is_palindrome_recursive(a)
print is_palindrome_iterative(a)
