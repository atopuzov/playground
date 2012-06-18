def find_number_xor(l):
    res = 0
    for i in l:
        res ^= i
    # res = reduce(lambda x,y: x^y, l)
    return res

def find_number_ht(l):
    ht = {}
    for i in l:
        ht[i] = ht.get(i, 0) + 1

    for key,val in ht.items():
        if val % 2 == 1:
            return key

def find_number_two_ht(l):
    nums = []
    ht = {}
    for i in l:
        ht[i] = ht.get(i, 0) + 1

    for key,val in ht.items():
        if val % 2 == 1:
            nums.append(key)

    return nums

def find_number_two_xor(l):
    x = y = 0
    xory = reduce(lambda x,y: x^y, l)
    set_bit = xory & ~(xory-1)

    for i in l:
        if i & set_bit:
            x ^= i
        else:
            y ^= i
    return [x,y]

l = [1,1,2,2,3,3,3,3,4]

print find_number_xor(l)
print find_number_ht(l)

k = [2,2,2,2,3,3,3,3,4,5,5,5,6,6]

print find_number_two_ht(k)
print find_number_two_xor(k)
