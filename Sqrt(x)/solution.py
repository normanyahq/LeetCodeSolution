class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l, r = 0, x
        while l<=r:
            mid = (l + r) // 2
            t = mid ** 2
            if t == x:
                return mid
            elif t < x:
                l = mid + 1
            else:
                r = mid - 1
        return l if l ** 2 <= x else l - 1
