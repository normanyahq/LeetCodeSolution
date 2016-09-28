from collections import defaultdict
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        c_count = defaultdict(int)
        if not s:
            return 0
        for c in s:
            c_count[c] += 1
        c, count = min([(c, v) for c, v in c_count.items()], key=lambda x: x[1])
        if count >= k:
            return len(s)
        else:
            return max([self.longestSubstring(t, k) for t in s.split(c)])
