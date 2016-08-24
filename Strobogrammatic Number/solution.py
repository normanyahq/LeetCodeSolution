class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        num = str(num)
        left = 0
        right = len(num)-1
        while (num[left] == num[right] and num[left] in ['0', '1', '8'] or int (num[left]) * int (num[right]) == 6 * 9) and left < right:
            left += 1
            right -= 1
        if left == right and num[left] in ['1', '8', '0'] or left - 1 == right:
            return True
        else:
            return False
