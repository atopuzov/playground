def is_substring_naive(string, sub):
    for i in xrange(len(string)-len(sub)+1):
        for j in xrange(len(sub)):
            if string[i+j] == sub[j]:
                if j == len(sub)-1:
                    return True, i
            else:
                break
    return False, 0

def is_substring_rk(string, sub):
    sub_hash = rk_hash(sub)
    string_hash = rk_hash(string[:len(sub)])
    for i in xrange(len(string)-len(sub)+1):
        if string_hash == sub_hash:
            return True,i
        else:
            string_hash = rk_hash(string[i+1:i+1+len(sub)])
    return False, 0

def rk_hash(string, base=101):
    h = 0
    for i in xrange(len(string)):
        h += ord(string[-(1+i)])*base**i
    return h

def is_substring_kmp(string, sub):
    m = 0
    i = 0
    t = kmp_table(sub)
    while m+i < len(string):
        if string[m+i] == sub[i]:
            if i == len(sub)-1:
                return True, m
            i += 1
        else:
            m += i - t[i]
            if t[i] > -1:
                i = t[i]
            else:
                i = 0
    return False, 0

def kmp_table(string):
    t = [-1] + [0]*(len(string)-1)
    pos = 2
    cnd = 0
    while pos < len(string):
        if string[pos-1] == string[cnd]:
            cnd += 1
            t[pos] = cnd
            pos += 1
        elif cnd > 0:
            cnd = t[cnd]
        else:
            t[pos] = 0
            pos += 1

    return t

a = "this is a very long string"
b = "very"
print is_substring_naive(a,b)
print is_substring_rk(a,b)
print is_substring_kmp(a,b)
