class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        pos_dict = dict()
        result_set = set()
        nums.sort()
        for i, v in enumerate(nums):
            pos_dict[v] = i
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                s = - nums[i] - nums[j]
                if pos_dict.get(s, -1) > j:
                    result_set.add((nums[i], nums[j], s,))
        return [list(i) for i in result_set]

