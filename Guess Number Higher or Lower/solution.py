# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left <= right:
            mid = (left + right) / 2
            r = guess(mid)
            if not r:
                return mid
            elif r > 0:
                left = mid + 1
            else:
                right = mid - 1
        
