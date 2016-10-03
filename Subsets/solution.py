class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = list()
        set_size = 1 << (len(nums))
        for i in xrange(set_size):
            t = list()
            for j in xrange(set_size):
                if (i>>j) & 1:
                    t.append(nums[j])
            result.append(t)
        return result
