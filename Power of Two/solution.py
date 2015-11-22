class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if not n:
            return False
        while not n % 2:
            n >>= 1
        return n == 1
