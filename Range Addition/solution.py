class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        arr = [0] * (length + 1)
        for s, e, v in updates:
            arr[s] += v
            arr[e+1] -= v
        for i in xrange(1, length):
            arr[i] += arr[i-1]
        arr.pop()
        return arr
        
