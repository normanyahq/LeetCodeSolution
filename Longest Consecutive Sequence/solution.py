
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        result = 1
        for n in nums:
            if n-1 not in nums:
                m = n + 1
                while m in nums:
                    m += 1
                if m - n > result:
                    result = m - n
        return result