class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        n += 1
        sqrt5 = math.sqrt(5)
        return int (round (1./sqrt5 * ((1 + sqrt5)/2)**n - ((1-sqrt5)/2)**n, 0))
        
