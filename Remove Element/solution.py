class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        ans = len(nums)
        begin = 0
        end = len(nums) - 1
        while begin <= end:
            while begin <= end and nums[begin] != val:
                begin += 1
            while end >= begin and nums[end] == val:
                end -= 1
                ans -= 1
            if begin <= end:
                nums[begin], nums[end] = nums[end], nums[begin]
        nums = nums[:ans]
        return ans
        
