class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result = 0
        nums.sort()
        for i in range(0, len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                t_sum = nums[i] + nums[j]
                while k > j and nums[k] + t_sum >= target:
                    k -= 1
                result += k-j
                j += 1
        return result
