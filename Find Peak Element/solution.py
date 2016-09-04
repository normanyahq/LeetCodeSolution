class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.insert(0, float('-Inf'))
        nums.append(float('-Inf'))
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid - 1
            elif nums[mid] < nums[mid-1] and nums[mid] > nums[mid+1]:
                right = mid - 1
            else:
                left = mid + 1
        return mid - 1
