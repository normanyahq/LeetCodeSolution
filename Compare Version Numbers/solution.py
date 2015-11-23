class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1 += ".0" if '.' not in version1 else ""
        version2 += ".0" if '.' not in version2 else ""
        
        v1 = map(lambda x: int(x), version1.split('.'))
        v2 = map(lambda x: int(x), version2.split('.'))
        if len (v1) != len(v2):
            diff = abs(len (v1) - len(v2))
            if len(v1) > len(v2):
                v2.extend([0] * diff)
            else:
                v1.extend([0] * diff)
        if v1 > v2:
            return 1
        elif v1 < v2:
            return -1
        else:
            return 0
