from collections import defaultdict
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        f = defaultdict(int)
        f[-1] = 1
        if s[0] > "0" and s[0] <= "9":
            f[0] = 1
        for i in xrange(1, len(s)):
            if s[i] > "0":
                f[i] = f[i-1]
            if s[i-1:i+1] >= "10" and s[i-1:i+1] <= "26":
                f[i] += f[i-2]
        return f[len(s)-1]
