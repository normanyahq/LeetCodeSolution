import bisect
import random
class Solution(object):
    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type numsSize: int
        """
        nums = [(v, i) for i, v in enumerate(nums)]
        self.arr = sorted(nums)

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        l = bisect.bisect_left(self.arr, (target, 0))
        r = bisect.bisect_right(self.arr, (target, float('Inf'))) - 1
        idx = random.randint(l, r)
        return self.arr[idx][1]

