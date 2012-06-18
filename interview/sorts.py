def sort_selection(a):
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            if a[j] < a[i]:
                a[i], a[j] = a[j], a[i]

def sort_bubble(a):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(a)-1):
            if p[i+1] < p[i]:
                a[i], a[i+1] = a[i+1], a[i]
                swapped = True

p = [4,1,3,2,5]
sort_selection(p)
print p

p = [4,1,3,2,5]
sort_bubble(p)
print p
