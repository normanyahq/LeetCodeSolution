class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        i = 1
        while i+1 < len(nums):
            nums[i], nums[i+1] = nums[i+1], nums[i]
            i += 2
