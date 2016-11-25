class Solution(object):
    _cache = dict()
    @staticmethod
    def f(i, j):
        if i >= j:
            return 0
        if i == j-1:
            return min(i, j)
        if (i, j) in Solution._cache:
            return Solution._cache[i, j]
        for k in xrange(i, j+1):
            if (i, j) not in Solution._cache or Solution._cache[i, j] > k + max(Solution.f(i, k-1), Solution.f(k+1, j)):
                Solution._cache[i, j] = k + max(Solution.f(i, k-1), Solution.f(k+1, j))
        return Solution._cache[i, j]
        
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        return Solution.f(1, n)
