class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        pos = 0
        answer = []
        while pos < len(nums):
            end = pos + 1
            while end < len(nums) and nums[end] == nums[pos] + end-pos:
                end += 1
            if end-1 != pos:
                answer.append("%d->%d" % (nums[pos], nums[end-1]))
            else:
                answer.append("%d" % nums[pos])
            pos = end
        return answer
