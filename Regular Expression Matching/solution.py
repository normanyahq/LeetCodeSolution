from collections import defaultdict, deque

class Solution(object):
    def __init__(self):
        self.cached = dict()
        
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if p == "":
            return s == ""
        if s == "":
            if p[-1] == "*":
                return self.isMatch(s, p[:-2])
            else:
                return False
        if (s, p) in self.cached:
            return self.cached[s, p]
        result = False
        if p[-1] == ".":
            result = self.isMatch(s[:-1], p[:-1])
        elif p[-1] == '*':
            flag = self.isMatch(s, p[:-2])
            i = len(s) - 1
            while not flag and i >= 0 and (s[i] == p[-2] or p[-2] == '.'):
                flag = self.isMatch(s[:i], p[:-2])
                i -= 1
            result = flag
        else:
            result = (p[-1] == s[-1] or p[-1] == '.') and self.isMatch(s[:-1], p[:-1])
        self.cached[s, p] = result
        return result
            
                

                    
        
        
