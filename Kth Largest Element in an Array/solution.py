import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        h = list()
        for i in xrange(k):
            heapq.heappush(h, nums[i])
        for i in xrange(k, len(nums)):
            if nums[i] > h[0]:
                heapq.heappop(h)
                heapq.heappush(h, nums[i])
        return h[0]
