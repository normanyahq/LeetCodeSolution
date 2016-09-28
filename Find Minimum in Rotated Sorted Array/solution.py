class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        if nums[left] <= nums[right]:
            return nums[left]
        while left <= right:
            print left, right
            if (right - left) <= 3:
                return min(nums[left:right+1])
            mid = (left + right) / 2
            if nums[mid] < nums[mid-1] and nums[mid] < nums[mid+1]:
                return nums[mid]
            elif nums[mid] > nums[left] and nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[left] and nums[mid] < nums[right]:
                right = mid - 1
            else:
                return nums[left]

