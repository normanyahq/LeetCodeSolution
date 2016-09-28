from collections import defaultdict
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        char_count = defaultdict(int)
        for c in s:
            char_count[c] += 1
        left = 0
        new_t = ""
        while left < len(t):
            right = left+1
            while right < len(t) and t[left] == t[right]:
                right += 1
            new_t += t[left] * min(right - left, char_count[t[left]])
            left = right
        t = new_t
            
        f = defaultdict(bool)
        for i in range(len(t) + 1):
            f[0, i] = True
        for i in xrange(1, len(s)+1):
            for j in xrange(1, len(t)+1):
                if s[i-1] == t[j-1] and f[i-1, j-1] or f[i, j-1]:
                    f[i, j] = True
        return f[len(s), len(t)]
        
