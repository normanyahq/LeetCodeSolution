class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fast_pos = 0
        slow_pos = 1
        if not nums or len(nums) == 1:
            return len(nums)
        while slow_pos < len(nums) - 1 and nums[slow_pos] != nums[slow_pos - 1]:
            slow_pos += 1
        fast_pos = slow_pos
        while fast_pos < len(nums):
            while fast_pos < len(nums) and nums[fast_pos] == nums[fast_pos - 1]:
                fast_pos += 1
            if fast_pos == len(nums):
                break
            nums[slow_pos] = nums[fast_pos]
            slow_pos += 1
            fast_pos += 1
        nums = nums[:slow_pos]
        return slow_pos
            
