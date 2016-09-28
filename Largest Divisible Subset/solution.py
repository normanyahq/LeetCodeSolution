class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return nums
        dp = list()
        prev = list()
        nums.sort()
        max_size = 1
        end_val = nums[0]
        end_idx = 0
        for i in range(len(nums)):
            dp.append(1)
            prev.append(0)
            for j in range(i-1, -1, -1):
                if nums[i] % nums[j]:
                    continue
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
                    if dp[i] >= max_size:
                        max_size = dp[i]
                        end_val = nums[i]
                        end_idx = i
                        
        result = list()
        while max_size:
            result.append(nums[end_idx])
            max_size -= 1
            end_idx = prev[end_idx]
        return result
                
        
