class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left = 0
        right = 0
        max_len = 0
        if k < 1:
            return 0
        char_count = dict()
        while right < len(s):
            count = char_count.get(s[right], 0)
            count += 1
            char_count[s[right]] = count
            if count == 1 and len(char_count) > k:
                while True:
                    char_count[s[left]] -= 1
                    if not char_count[s[left]]:
                        del char_count[s[left]]
                        break
                    left += 1
                left += 1
            max_len = max(max_len, right - left + 1)
            right += 1
        return max_len
        
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.lengthOfLongestSubstringKDistinct(s, 2)
