class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        i = 0
        j = 1
        to_add = 0
        while j <= n:
            if i < len(nums) and nums[i] <= j:
                j += nums[i]
                i += 1
            else:
                to_add += 1
                j += j
        return to_add

