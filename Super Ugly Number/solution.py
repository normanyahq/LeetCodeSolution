class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        index = [0] * len(primes)
        result = [1] + [float('Inf')] * (n - 1)
        for i in range(1, n):
            for j in range(len(primes)):
                if result[index[j]] * primes[j] < result[i]:
                    result[i] = result[index[j]] * primes[j]
            for j in range(len(primes)):
                if result[index[j]] * primes[j] == result[i]:
                    index[j] += 1
        return result[-1]
