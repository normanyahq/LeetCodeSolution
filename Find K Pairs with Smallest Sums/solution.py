import heapq
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        heap = list()
        for i in nums1[:min(k, len(nums1))]:
            for j in nums2:
                if len(heap) < k or -(i+j) > heap[0][0]:
                    heapq.heappush(heap, [-(i+j), i, j])
                if len(heap) > k:
                    heapq.heappop(heap)
        return [[i[1], i[2]] for i in heap]
