def isRotation(s1,s2):
    if len(s1) != len(s2):
        return False
    else:
        s = s1 + s1
        return isSubstring(s,s2)

def isSubstring(s1,s2):
    if s1.find(s2) == -1:
        return False
    else:
        return True

s1 = 'waterbottle'
s2 = 'erbottlewat'

print s1, s2, isRotation(s1,s2)

