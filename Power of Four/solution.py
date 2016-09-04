class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        binNum = bin(num)[2:]
        return (not binNum.count('0') % 2) and binNum.count('1') == 1 and num > 0
