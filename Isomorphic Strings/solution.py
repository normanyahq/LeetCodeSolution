class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s2t = {}
        t2s = {}
        for i,j in zip(s, t):
            if i in s2t:
                if s2t[i] != j:
                    return False
            else:
                s2t[i] = j
            if j in t2s:
                if t2s[j] != i:
                    return False
            else:
                t2s[j] = i
            
                
        return True
