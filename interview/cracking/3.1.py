
class StackInAnArray():
    def __init__(self):
        self.size = 100
        self.a = [' ']*3*self.size
        self.p = [0,0,0]

    def addr(self, s):
        return s*self.size  + self.p[s]
        
    def push(self, s, v):
        m = self.addr(s)

        self.a[m] = v
        self.p[s] += 1

    def pop(self, s):
        self.p[s] -= 1
        m = self.addr(s)
        e = self.a[m]
        self.a[m] = ' '
        return e

    def peek(self, s):
        m = self.addr(s) - 1
        return self.a[m]

    def __repr__(self):
        return str(self.a) + " " + str(self.p)

s = StackInAnArray()
s.push(0,'a')
s.push(1,'b')
x = s.pop(1)
print s, x, s.peek(0)
