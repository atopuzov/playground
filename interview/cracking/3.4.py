class Tower():
    def __init__(self, r=3, d=4):
        self.rods = []
        for i in xrange(r):
            self.rods.append([])
        for i in reversed(xrange(d)):
            self.rods[0].append(i)
        self.r = r
        self.d = d

    def __repr__(self):
        s = ""
        for i in reversed(xrange(self.d)):
            for j in xrange(self.r):
                if len(self.rods[j]) > i:
                    e = str(self.rods[j][i])
                    s += e + " " * (4-len(e)+1)
                else:
                    s += "|" + " " * 4 
            s += "\n"
        return s

    def moveDisc(self, r1,r2):
        if self.rods[r2] == [] or self.rods[r2][-1] > self.rods[r1][-1]:
            self.rods[r2].append(self.rods[r1].pop())
            return True
        return False

    def move(self, n, source, destination, spare):
        if n == 1:
            self.moveDisc(source, destination)
            # print self
        else:
            self.move(n-1, source, spare, destination)
            self.moveDisc(source, destination)
            # print self
            self.move(n-1, spare, destination, source) 
    def solve(self):
        self.move(self.d, 0, 2, 1)

t = Tower(d = 3)
print t
t.solve()
print t
