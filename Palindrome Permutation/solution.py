class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        odd_count = 0
        char_count = dict()
        for i in s:
            char_count[i] = char_count.get(i, 0) + 1
            if char_count[i] % 2:
                odd_count += 1
            else:
                odd_count -= 1
        return odd_count <= 1
