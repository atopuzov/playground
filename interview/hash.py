
def hash(key, base=256):
    return key % 256 

def hash2(key, base=256):
    k = 0
    for i in xrange(len(key)):
        k += ord(key[i])*base**i

    return k % base

class ht:
    def __init__(self, base=256):
        self.a = [None] * base
        self.base = base

    def get(self, key):
        return self.a[hash(key, self.base)]

    def set(self, key, value):
        self.a[hash(key, self.base)] = value

    def __repr__(self):
        s = ""
        for i in xrange(self.base):
            s += str(self.a[i]) + " "
        return s


h = ht()
h.set(500,'aco')
h.set(540,'coa')


