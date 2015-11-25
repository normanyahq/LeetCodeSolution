# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right, mid = 1, n, (1+n)//2
        _isBadVersion = False
        while left <= right:
            mid = (left + right)//2
            _isBadVersion = isBadVersion(mid)
            if _isBadVersion:
                right = mid - 1
            else:
                left = mid + 1
        return mid if _isBadVersion else mid + 1
            
