def removeDuplicateChar(s):
    '''Uses bit vectors to keep track of duplicate chars'''
    if len(s) < 2:
        return s
    else:
        k = 0
        duplicate = 0
        '''Find duplicate charachters'''
        for c in s:
            bit = 1 << ord(c)
            if k & bit == bit:
                duplicate = duplicate | bit
            k = k | bit
        done = duplicate

        '''Print non-duplicate charachters and duplicate charachters only once'''
        result = ""
        for c in s:
            bit = 1 << ord(c)
            if duplicate & bit == bit:
                if done & bit == bit:
                    done = done ^ bit
                    result += c
            else:
                result += c
        return result



s1 = "abcd"
s2 = "aaaa"
s3 = ""
s4 = "aaabbb"
print s1, removeDuplicateChar(s1)
print s2, removeDuplicateChar(s2)
print s3, removeDuplicateChar(s3)
print s4, removeDuplicateChar(s4)

