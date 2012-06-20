
def reverse_string_iterative(string):
    ret = ""
    n = len(string)
    for i in xrange(n):
        ret += string[n-i-1]
    return ret

def reverse_string_inplace(string):
    '''Not the best way to reverse a string python ;)'''
    ret = list(string)
    n = len(string)
    i = 0
    while i < n/2:
        ret[i], ret[n-i-1] = ret[n-i-1], ret[i]
        i+=1
    
    return "".join(ret)

def reverse_string_inplace_recursive(string):
    l = list(string)
    _reverse_string_inplace_recursive(l, 0)
    return "".join(l)

def _reverse_string_inplace_recursive(a,i):
    n = len(a)
    if i >= n/2:
        return
    if n >= 2:
        a[i], a[n-1-i] = a[n-1-i], a[i]
        i += 1
        _reverse_string_inplace_recursive(a,i)

def reverse_string_recursive(string):
    if len(string)<2:
        return string
    else:
        return string[-1] + reverse_string_recursive(string[0:-1])

def reverse_string_with_a_stack(string):
    st = []
    for s in string:
        st.append(s)
    r = ""
    while st:
        r += st.pop()
    return r


s = "Aleksandar"

print reverse_string_iterative(s)
print reverse_string_inplace(s)
print reverse_string_recursive(s)
print reverse_string_with_a_stack(s)
print reverse_string_inplace_recursive(s)

