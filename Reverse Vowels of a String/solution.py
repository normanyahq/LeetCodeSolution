class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        left = 0
        right = len(s) - 1
        vowel = ['a', 'e', 'i', 'o', 'u']
        while left < right:
            while left < right and s[left].lower() not in vowel:
                left += 1
            while left < right and s[right].lower() not in vowel:
                right -= 1
            if s[left].lower() in vowel and s[right].lower() in vowel:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        return "".join(s)
