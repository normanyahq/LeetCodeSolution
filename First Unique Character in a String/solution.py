from collections import defaultdict
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_count = defaultdict(int)
        for c in s:
            char_count[c] += 1
        for i, c in enumerate(s):
            if char_count[c] == 1:
                return i
        return -1
