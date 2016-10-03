from collections import defaultdict
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result_set = set()
        result = list()
        nums.sort()
        set_size = 1 << (len(nums))
        for i in xrange(set_size):
            t = list()
            for j in xrange(set_size):
                if (i>>j) & 1:
                    t.append(nums[j])
            tt = tuple(t)
            if tt not in result_set:
                result_set.add(tt)
                result.append(t)
        return result        
