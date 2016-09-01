class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        j = len(nums)-1
        while j and nums[j] <= nums[j-1]:
            j -= 1
        if j:
            t = j
            while t < len(nums)-1 and nums[t+1] > nums[j-1]:
                t += 1
            if t < len(nums):
                nums[t], nums[j-1] = nums[j-1], nums[t]
            l = j
            r = len(nums) -1
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        else:
            l = 0
            r = len(nums) -1
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        
