class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations or citations[-1] == 0:
            return 0
        n = len(citations)
        left = 0
        right = len(citations) - 1
        while left <= right:
            mid = (left + right) / 2
            if citations[mid] < n - mid:
                left = mid + 1
            else:
                if mid - 1 < 0 or n - mid + 1 > citations[mid - 1]:
                    return n - mid
                else:
                    right = mid - 1
        return n - mid
