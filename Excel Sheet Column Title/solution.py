class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ""
        while n:
            result = chr(((n-1) % 26) + ord('A')) + result
            n = (n - ((n-1)%26)) / 26
        return result
