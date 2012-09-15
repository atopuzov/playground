def isAnagram(s1,s2):
    a = list(s1)
    b = list(s2)
    a.sort()
    b.sort()
    return a == b
    
def isAnagram2(s1,s2):
    if len(s1) != len(s2):
        return False
    n = len(s1)
    for i in xrange(n):
        if s1[i] != s2[n-i-1]:
            return False
    return True

s1 = "aleksandar"
s2 = "radnaskela"

print s1,s2,isAnagram(s1,s2),isAnagram2(s1,s2)

s1 = "aleksandar"
s2 = "kilimanjar"
print s1,s2,isAnagram(s1,s2),isAnagram2(s1,s2)

