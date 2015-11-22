class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        appeared = set([n])
        while True:
            n = self.digitSqureSum(n)
            if n == 1:
                return True
            if n in appeared:
                return False
            appeared.add(n)
        
    def digitSqureSum(self, x):
        result = 0
        while x:
            result += (x % 10) ** 2
            x /= 10
        return result
