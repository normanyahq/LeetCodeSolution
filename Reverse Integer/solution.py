class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = int(("" if x>0 else "-") + "".join(reversed(str(abs(x)))))
        return 0 if result > ((1<<31)-1) or result < -(1<<31) else result
