class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        volumn = 0
        left = 0
        right = len(height) - 1
        while left < right:
            min_height = height[left]
            if height[left] <= height[right]:
                while height[left] <= min_height and left < right:
                    volumn += -height[left] + min_height if height[left] < min_height else 0
                    left += 1
            else:
                min_height = height[right]
                while height[right] <= min_height and left < right:
                    volumn += -height[right] + min_height if height[right] < min_height else 0
                    right -= 1
        return volumn
