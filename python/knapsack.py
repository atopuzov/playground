#!/usr/bin/env python
# (c) 2013 Aleksandar Topuzovic <aleksandar.topuzovic@gmail.com>
import collections

def knapscak(items, W):
    '''
    Solves the knapsack problem

    :param items: Iterable containing the items
    :param W: Maximum weight
    '''
    A = {(0, x): 0 for x in xrange(W + 1)}
    for i, item in enumerate(items, 1):
        for x in xrange(W + 1):
            if item.weight > x:
                A[(i, x)] = A[(i - 1, x)]
            else:
                A[(i, x)] = max(A[(i - 1, x)],
                                A[(i - 1, x - item.weight)] + item.value)

    x = W
    result = []
    for i, item in reversed(list(enumerate(items, 1))):
        if A[(i, x)] != A[(i - 1, x)]:
            result.append(item)
            x -= item.weight

    maximum_value = A[(len(items), W)]
    return maximum_value, result


if __name__ == '__main__':
    item = collections.namedtuple('item', 'value weight')
    items = [
        item(3, 4),
        item(2, 3),
        item(4, 2),
        item(4, 3),
    ]
    max_value, selected_items = knapscak(items, 6)

    print 'Items: {}'.format(', '.join(map(str, items)))
    print 'Selected items: {}, maximum value: {}'.format(', '.join(map(str, selected_items)), max_value)
