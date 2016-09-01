class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(key=lambda x: -x)
        
        i = 0
        while i < len(citations):
            if citations[i] < i + 1:
                return i
            i += 1
        return 0 if i != len(citations) else i
        
