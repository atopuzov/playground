def coins(sum, denominations):
    result = [0] + [999]*sum

    for csum in xrange(1,sum+1):
        for j in xrange(0, len(denominations)):
            ref = result[csum - denominations[j]] + 1
            if denominations[j] <= csum and ref < result[csum]:
                tempA = result[csum - denominations[j]]
                tempB = tempA+1
                result[csum] = tempB
        return result[sum]

print coins(15, [1,2,3,5])

    
