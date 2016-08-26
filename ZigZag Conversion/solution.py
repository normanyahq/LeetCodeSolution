class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        group_size = 2 * numRows - 2
        result = ""
        for i in xrange(len(s) / group_size + 1):
            idx = i * group_size
            if len(s) > idx:
                result += s[idx]
        for k in xrange(1, numRows - 1):
            for i in xrange(len(s) / group_size + 1):
                idx = i * group_size + k
                if len(s) > idx:
                    result += s[idx]
                idx = i * group_size + group_size - k
                if len(s) > idx:
                    result += s[idx]
        for i in xrange(len(s) / group_size + 1):
            idx = i * group_size + numRows - 1
            if len(s) > idx:
                result += s[idx]
        return result
