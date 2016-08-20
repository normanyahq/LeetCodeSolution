class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        nums = sorted(list(set(nums)))
        if not len(nums):
            if lower != upper:
                return ["%d->%d" % (lower, upper)]
            else:
                return [str(lower)]
        result = []
        left_value = lower
        p = 0
        if nums[p] == lower:
            left_value += 1
        while p < len(nums):
            right_value = nums[p] - 1
            if right_value == left_value:
                result.append("%d" % left_value)
            elif right_value > left_value:
                result.append("%d->%d" % (left_value, right_value))
            left_value = nums[p] + 1
            p += 1
        if nums[-1] != upper:
            if nums[-1] + 1 == upper:
                result.append("%d" % upper)
            elif nums[-1] + 1 < upper:
                result.append("%d->%d" % (nums[-1] + 1, upper))

        return result
            
        
