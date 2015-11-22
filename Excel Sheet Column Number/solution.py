class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for c in s:
            digit = ord(c) - ord('A') + 1
            result = result * 26 + digit
        return result
