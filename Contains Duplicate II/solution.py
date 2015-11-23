class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not k:
            return False
        k += 1
        data = set()
        for i in range(0, min(k, len(nums))):
            if nums[i] in data:
                return True
            data.add(nums[i])
        if k<len(nums):
            for i in range(k, len(nums)):
                data.remove(nums[i-k])
                if nums[i] in data:
                    return True
                data.add(nums[i])
        return False
        
