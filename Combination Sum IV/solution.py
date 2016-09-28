from collections import defaultdict
class Solution(object):
    def __init__(self):
        self.cache = defaultdict(int)
    
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in self.cache:
            return self.cache[target]
        elif target == 0:
            return 1
        elif target < 0:
            return 0
        for num in nums:
            self.cache[target] += self.combinationSum4(nums, target - num)
        return self.cache[target]
        
        
