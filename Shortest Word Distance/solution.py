class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        last_word1 = -1
        last_word2 = -1
        min_dist = len(words)-1
        for i in range(len(words)):
            if words[i] == word1:
                last_word1 = i
                if last_word2 != -1:
                    min_dist = min(last_word1 - last_word2, min_dist)
            elif words[i] == word2:
                last_word2 = i
                if last_word1 != -1:
                    min_dist = min(last_word2 - last_word1, min_dist)
        return min_dist
                    
