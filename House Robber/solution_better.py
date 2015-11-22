class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=2:
            return max(nums + [0]) # deal with empty list
        f = {}
        f [0] = nums[0]
        f [1] = max(nums[0:2])
        for i in range (2, len(nums)):
            f[i] = max (f[i-1], f[i-2] + nums[i])
        return max (f[len(nums)-1], f[len(nums)-2])
