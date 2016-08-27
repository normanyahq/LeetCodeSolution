class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        arr = sorted(nums)
        left = (len(nums) - 1) / 2
        right = len(nums) - 1
        pos = 0
        while pos + 1 < len(nums):
            nums[pos], nums[pos+1] = arr[left], arr[right]
            left -= 1
            right -= 1
            pos += 2
        if pos < len(nums):
            nums[-1] = arr[left]
        

