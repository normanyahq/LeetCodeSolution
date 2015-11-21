class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num <= 9:
            return num
        else:
            return ((num-1) % 9 + 1)
