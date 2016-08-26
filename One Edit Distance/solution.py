class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        len_diff = len(s)-len(t)
        if abs(len_diff) >= 2:
            return False
        first_diff = 0
        while first_diff < min(len(s), len(t)) and s[first_diff] == t[first_diff]:
            first_diff += 1
        if not len_diff:
            return first_diff != len(s) and s[first_diff+1:] == t[first_diff+1:]
        elif len_diff == -1:
            return s[first_diff:] == t[first_diff+1:]
        else:
            return s[first_diff+1:] == t[first_diff:]
        
