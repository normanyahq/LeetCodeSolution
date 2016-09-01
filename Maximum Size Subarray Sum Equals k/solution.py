class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = 0
        left = 0
        right = len(nums) - 1
        s = [0] * (len(nums) + 1)
        idx_dict = dict({0:0})
        for i in xrange(len(nums)):
            s[i+1] = s[i] + nums[i]
            if -k + s[i+1] in idx_dict:
                result = max(result, i+1-idx_dict[-k + s[i+1]])
            if s[i+1] not in idx_dict:
                idx_dict[s[i+1]] = i+1

        return result
