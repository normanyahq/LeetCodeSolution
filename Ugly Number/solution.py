class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        factor_list = [2, 3, 5]
        for i in factor_list:
            while not num % i:
                num /= i
        return num == 1
