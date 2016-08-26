class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sorted_list = sorted([(v, i) for i, v in enumerate(nums)])
        left = 0
        right = len(nums) - 1
        while left < right:
            if sorted_list[left][0] + sorted_list[right][0] == target:
                return [sorted_list[left][1], sorted_list[right][1]]
            elif sorted_list[left][0] + sorted_list[right][0] < target:
                left += 1
            else:
                right -= 1
        
