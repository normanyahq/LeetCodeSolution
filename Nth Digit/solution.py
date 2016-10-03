class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 9:
            return n
        t = 9
        exp = 1
        total_digit = 9
        while total_digit + t * 10 * (exp + 1) < n:
            t *= 10
            exp += 1
            total_digit += exp * t
        
        t2 = n - total_digit
        kth = (t2 - 1) / (exp + 1)  + 10 ** exp
        b = exp - (t2 - 1) % (exp+1)
        return kth / (10**b) % 10

