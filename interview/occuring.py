
"""Write an algorithm to find the first non-repeated character in a string. For example, the first non-repeated character in the string abcdab is c"""

def naive(string):
    for i in range(len(string)):
        o = False
        for j in range(i+1,len(string)):
            if string[i] == string[j]:
                o = True
        if not o:
            return string[i]

def with_ht(string):
    o = {}
    for c in string:
        o[c] = o.get(c,0) + 1
    for k,v in o.items():
        if v==1:
            return k

s = "abcdab"
print naive(s)
print with_ht(s)
