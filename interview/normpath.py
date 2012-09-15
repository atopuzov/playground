"""
Normalize a path:
 - uses a stack
""" 

a = "/windows/abs/../temp/new/../"
p = a.split('/')

n = []
for d in p:
    print d
    if d == "..":
        n.pop()
    else:
        n.append(d)

print "/".join(n)
