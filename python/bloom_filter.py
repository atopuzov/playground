#!/usr/bin/env python
# (c) Aleksandar Topuzovic <aleksandar.topuzovic@gmail.com>
import math

class bf(object):
    '''
    Bloom-Filter data structire
    '''
    def __init__(self, n=20, k=0):
        '''
        Bloom Filter costructor

        @param n: number of bits
        @param k: number of hash functions (autocalculated if 0)
        '''
        self.a = [0 for _ in xrange(n)]  # List implementation
        #self.a = 0  # Bit implementation
        self.n = n
        if k == 0:
            self.k = int(math.log(2) * self.n)
        else:
            self.k = k

    def __str__(self):
        '''
        String representaion of the bloom filter
        '''
        return "Bits: {}, hash functions: {}, error rate: {}%".format(self.n, self.k, (1.0/2.0) ** (math.log(2) * self.n) * 100)

    def hash(self, k, item):
        '''
        Emulating multiple hash functions with one function by using it multiple times

        @param k: Number of the hash function:
        @param item: Item to hash
        '''
        h = hash(item)
        for _ in xrange(k-1):
            h = hash(str(h))

        return h % self.n

    def insert(self, item):
        '''
        Inserts an intem into a bloom filter

        @param item: Item to insert
        '''
        for i in xrange(self.n):
            x = self.hash(i % self.k, item)

            if type(self.a) == list:  # List implementation
                self.a[x] = 1
            elif type(self.a) == int:  # Bit implementation
                self.a = self.a | 1 << x

    def isin(self, item):
        '''
        Checks weather an object is in the filter
        
        @param item: Item to check for
        '''
        for i in xrange(self.k):
            x = self.hash(i % self.k, item)

            if type(self.a) == list:
                if self.a[x] != 1:
                    return False
            elif type(self.a) == int:
                if self.a & 1 << x != 1 << x:
                    return False
        return True

if __name__ == '__main__':
    b = bf(n=40)
    print b
    
    inserts = ['aco', 'maca', 'more']
    for i in inserts:
        b.insert(i)

    tests = ['aco', 'maca', 'grancikula', 'jez', 'sunce', 'more', 'lavanda']
    expected_results = [True, True, False, False, False, True, False]
    results = [b.isin(t) for t in tests]
    
    if expected_results == results:
        print "All ok"
    else:
        print "Something went wrong"
