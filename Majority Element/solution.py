class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_count = 1
        num = nums[0]
        for n in nums[1:]:
            if num == n:
                num_count += 1
            else:
                num_count -= 1
            if num_count == 0:
                num = n
                num_count = 1
        return num
