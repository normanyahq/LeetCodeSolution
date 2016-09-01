class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        n = len(nums)-1
        while j <= n:
            if nums[j] < 1:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
                i += 1
            elif nums[j] > 1:
                nums[n], nums[j] = nums[j], nums[n]
                n -= 1
            else:
                j += 1
