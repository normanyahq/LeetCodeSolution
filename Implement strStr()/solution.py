class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
    # allow indexing into needle and protect against change during yield
        if not needle:
            return 0
        needle = list(needle)
    
        # build table of shift amounts
        shifts = [1] * (len(needle) + 1)
        shift = 1
        for pos in range(len(needle)):
            while shift <= pos and needle[pos] != needle[pos-shift]:
                shift += shifts[pos-shift]
            shifts[pos+1] = shift
    
        # do the actual search
        startPos = 0
        matchLen = 0
        for c in haystack:
            while matchLen == len(needle) or \
                  matchLen >= 0 and needle[matchLen] != c:
                startPos += shifts[matchLen]
                matchLen -= shifts[matchLen]
            matchLen += 1
            if matchLen == len(needle):
                return startPos
        return -1
