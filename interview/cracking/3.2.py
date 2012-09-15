class StackWithAMin():
    def __init__(self):
        self.s = []
        self.m = []

    def __repr__(self):
        return str(self.s) + " " + str(self.m)

    def push(self,v):
        self.s.append(v)
        if len(self.m) == 0 or v <= self.m[-1]:
            self.m.append(v)

    def pop(self):
        e = self.s.pop()
        if e == self.min():
            self.m.pop()

    def min(self):
        if len(self.m)>0:
            return self.m[-1]
        return None

s = StackWithAMin()
for e in [3,2,5,5,1,6,1]:
    s.push(e)
print s
print s.min()
s.pop()
print s
s.pop()
print s
s.pop()
print s.min()
print s
