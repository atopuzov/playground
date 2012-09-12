def sort_selection(_a):
    a = _a
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            if a[j] < a[i]:
                a[i], a[j] = a[j], a[i]
    return a

def sort_bubble(_a):
    a = _a
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(a)-1):
            if p[i+1] < p[i]:
                a[i], a[i+1] = a[i+1], a[i]
                swapped = True
    return a

def sort_merge(a):
    if len(a) < 2:
        return a
    else:
        m = len(a)/2
        left = sort_merge(a[:m])
        right = sort_merge(a[m:])
        r = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                r.append(left[i])
                i += 1
            else:
                r.append(right[j])
                j += 1
        r += left[i:]
        r += right[j:]
        return r

def sort_quick(a):
    if len(a) == 0:
        return []
 
    pivot = a[0]
    return [k for k in a[1:] if k<pivot] [pivot] +[k for k in a[1:] if k>=pivot]

def sort_insertion(_a):
    a = _a
    insertions = 0
    for i in range(1,len(a)):
        val = a[i]
        j = i-1;
        while j>=0 and a[j]>val:
            a[j+1] = a[j]
            j-=1
            insertions+=1
        a[j+1] = val
    return a

p = [4,1,3,2,5]
print sort_selection(p)
print sort_bubble(p)
print sort_merge(p)
print sort_quick(p)
print sort_insertion(p)
