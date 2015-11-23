
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=3:
            return int(n==3)
        isPrime = [False, True] * ((n+2) >> 1) # all even numbers are set to 0
        isPrime[0:3] = 0, 0, 1
        countPrime = 1
        for i in xrange(3, n, 2):
            #print i, isPrime[i]
            if isPrime[i]:
                countPrime += 1
                t = 2 * i
                while t < n:
                    isPrime[t] = False
                    t += i
        return countPrime

