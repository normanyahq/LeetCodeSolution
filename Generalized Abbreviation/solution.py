class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        result = []
        n_bits = len(word)
        for i in range(1<<n_bits):
            left = 0
            t_str = ""
            while left < len(word):
                if i >> (len(word) - left - 1) & 1:
                    right = left + 1
                    while right < len(word) and i >> (len(word) - right - 1) & 1:
                        right += 1
                    t_str += str(right - left)
                    left = right
                else:
                    t_str += word[left]
                    left += 1
            result.append(t_str)
        return result
