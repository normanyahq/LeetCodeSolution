class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            new_volumn = min(height[left], height[right]) * (right-left)
            max_area = max_area if new_volumn < max_area else new_volumn
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
