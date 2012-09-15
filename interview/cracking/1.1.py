
def isUniqueChars(s):
    '''Using a dictionary: space complexity O(n), time complexity O(n)'''
    e = {}
    for c in s:
        if e.get(c,False):
            return False
        e[c] = True
    return True

def isUniqueChars2(s):
    '''Using a bit vector: space complexity O(1), time complexity O(n)'''
    k = 0
    for c in s:
        b = 1 << ord(c)
        if k & b == b:
            return False
        k = k | b
    return True

def isUniqueChars3(s):
    '''Using 2 loops: space complexity O(0), time complexity O(n^2)'''
    for i in xrange(0, len(s)):
        for j in xrange(i+1, len(s)-1):
            if s[i] == s[j]:
                return False
    return True

def isUniqueChars4(s):
    '''Using sort and going trough the list: space complexity O(n), time complexity O(n*log(n))'''
    a = list(s)
    a.sort()
    for i in range(0, len(s)-1):
        if a[i] == a[i+1]:
            return False
    return True

s1 = 'Aleksandr'
s2 = 'This has some duplicate chars'

print s1, isUniqueChars(s1), isUniqueChars2(s1), isUniqueChars3(s1), isUniqueChars4(s1)
print s2, isUniqueChars(s2), isUniqueChars2(s2), isUniqueChars3(s2), isUniqueChars4(s2)
