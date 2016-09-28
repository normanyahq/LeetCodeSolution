import bisect
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        left = 0
        i = 0
        while left < len(nums):
            t_len = 1
            right = left + t_len
            while right < len(nums) and nums[right] == nums[left]:
                t_len *= 2
                right += t_len
            right = min(len(nums), right)
            idx = bisect.bisect_right(nums, nums[left], left, right)
            t = 1
            nums[i:i+t] = [nums[left]] * t
            i += t
            count += 1
            left = idx
        return count
            
