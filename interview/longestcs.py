
def find_longest_continous_sequence(s):
    if len(s) == 1:
        return 0,0
    else:
        r = []
        for i in range(1,len(s)-1):
            if s[i] < s[i-1]:
                r.append(i)
        p = 0
        t = 0
        b = 0
        for i in r:
            print i, p, i-p, t-b, t, b
            if i-p>t-b:
                t = i
                b = p
            p = i
        return b,t


s = [1,2,3,4,7,6,5,1,2,3,4,5,6,7,8,9,1,2,3]
i,j = find_longest_continous_sequence(s)
print i, j, s[i:j]
        
