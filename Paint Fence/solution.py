class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        f = [0] * max((n+1), 3)
        f[1] = k
        f[2] = k**2
        for i in range(3, n+1):
            f[i] = (k-1)*(f[i-1] + f[i-2])
        return f[n]
