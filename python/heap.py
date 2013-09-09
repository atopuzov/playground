#!/usr/bin/env python
# (c) Aleksandar Topuzovic <aleksandar.topuzovic@gmail.com>

class heap(object):
    '''Simple healp implementation using a list'''
    def __init__(self):
        self.data = []

    def push(self, item):
        '''
        Insert an item into the heap

        @param item: Item to insert
        '''
        i = len(self.data)
        self.data.append(item)

        while i > 0:
            p = i/2  # Parent
            if self.data[i] < self.data[p]:  # Bubble up
                self.data[p], self.data[i] = self.data[i], self.data[p]
                i = p
            else:
                break

    def pop(self):
        data = self.data[0]

        return data
                
    def __str__(self):
        '''String representation of the heap'''
        return ' '.join(map(str, self.data))

    def min(self):
        '''Minimum element in the heap'''
        try:
            return self.data[0]
        except IndexError:
            raise Exception('Empty heap')

    def as_list(self):
        return self.data

if __name__ == '__main__':
    h = heap()
    h.push(2)
    print h
    h.push(5)
    h.push(6)
    h.push(4)
    print h
    h.push(1)
    print h.min()
