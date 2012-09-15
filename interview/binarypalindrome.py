def bin_palindrome(b):
    k = 0
    o = b
    while o:
        k = (k << 1) | (o & 1)
        o = o >> 1
    return k == b

a = '101101'
b = int(a,2)
print bin_palindrome(b)
