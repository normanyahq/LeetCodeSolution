class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = "1"
        for i in range(0, n-1):
            pos = 0
            endpos = 0
            t = ""
            while pos<len(result):
                while endpos<len(result) and result[endpos]==result[pos]:
                    endpos += 1
                t += str(endpos-pos) + result[pos]
                pos = endpos
            result = t
        return result
