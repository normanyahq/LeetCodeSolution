class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        p2s, s2p = {}, {}
        
        pattern = list(pattern)
        str = str.split()
        if len(pattern) != len(str):
            return False
        for i, j in zip(pattern, str):
            if i in p2s:
                if p2s[i] != j:
                    return False
            else:
                p2s[i] = j
            if j in s2p:
                if s2p[j] != i:
                    return False
            else:
                s2p[j] = i
        return True
