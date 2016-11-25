from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = defaultdict(list)
        for word in strs:
            t = tuple(sorted(word))
            anagrams[t].append(word)
        return anagrams.values()
