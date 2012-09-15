def reverseString(s):
    '''Reverses a string using stack: space complexity O(n), time complexity O(n)'''
    stack = []
    for c in s:
        stack.append(c)
    result = ""
    while stack:
        result += stack.pop()
    return result

def reverseString2(s):
    '''Reverses string in place: space complexity O(0), time complexity O(n)'''
    a = list(s) # Python string are immuttable objects
    n = len(a)
    for i in range(0,n/2):
        a[i], a[n-i-1] = a[n-i-1], a[i]
    return "".join(a)

s = "Aleksandar"
print s, reverseString(s), reverseString2(s)

