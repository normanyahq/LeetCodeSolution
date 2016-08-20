class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = set()
        freqdict = dict()
        for i in nums:
            freqdict[i] = freqdict.get(i, 0) + 1
        nums = sorted(freqdict.keys())
        for i in range(len(nums)):
            j_start = i if freqdict[nums[i]] >= 2 else i+1
            for j in range(j_start, len(nums)):
                s = - nums[i] - nums[j]
                if s < nums[i] or s < nums[j] or s not in freqdict:
                    continue
                if nums[i] != nums[j] and nums[j] != s or \
                    nums[i] != nums[j] and nums[j] == s and freqdict[s] >=2 or \
                    nums[i] == s and nums[i] != nums[j] and freqdict[s] >= 2 or \
                    nums[i] == nums[j] and nums[i] != s and freqdict[nums[i]] >= 2 or \
                    nums[i] == nums[j] and nums[j] == s and freqdict[s] >= 3: 
                    result.add((nums[i], nums[j], s,))
        return [list(i) for i in result]

