class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        chars = zip(*strs)
        for i in chars:
            if len(set(i)) == 1:
                result += i[0]
            else:
                break
        return result
