class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        processed = []
        for c in s:
            c = c.lower()
            if c <= 'z' and c >= 'a' or c >= '0' and c <= '9':
                processed += c
        return sum(map(lambda x: x[0] != x[1], zip(processed, reversed(processed)))) == 0
