class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        target = s
        result = len(nums) + 1
        left = 0
        right = 1
        s = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            s[i+1] += s[i] + nums[i]
        print s
        while right <= len(nums):
            print left, right, s[right] - s[left]
            if s[right] - s[left] >= target:
                if right - left < result:
                    result = right - left
                left += 1
            elif s[right] - s[left] < target:
                right +=1
        return 0 if result > len(nums) else result
            
