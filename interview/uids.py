import re

f = open('/etc/passwd','r')

ht = {}
for l in f.readlines():
    if re.match("^#.*", l):
        continue
    t = l.split(':')
    username = t[0]
    uid = t[2]
    ht[uid] = ht.get(uid,[]) + [username]

for key,vals in ht.items():
    if len(vals)>1:
        print key + ":" + ','.join(vals)
