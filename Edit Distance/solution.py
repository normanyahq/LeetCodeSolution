class Solution(object):
    def __init__(self):
        self.f = dict()
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not len(word1) or not len(word2):
            return max(len(word1), len(word2))
        if (len(word1), len(word2),) in self.f:
            return self.f[len(word1), len(word2)]
        if word1[-1] == word2[-1]:
            self.f[len(word1), len(word2)] = self.minDistance(word1[:-1], word2[:-1])
        else:
            self.f[len(word1), len(word2)] = min(self.minDistance(word1[:-1], word2[:-1]), self.minDistance(word1[:-1], word2), self.minDistance(word1, word2[:-1])) + 1
        return self.f[len(word1), len(word2)]
