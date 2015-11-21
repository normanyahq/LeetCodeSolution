class Solution(object):
    def canWinNim_original(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n in [0, 1, 2, 3]:
            return n > 0
        f1, f2, f3, f4 = 1, 1, 1, 0
        for i in range (4, n+1):
            f4 = (min(f1, f2, f3)+1) % 2
            f1, f2, f3 = f2, f3, f4
        return f4 == 1
    def canWinNim(self, n):
        return n % 4 != 0
        

