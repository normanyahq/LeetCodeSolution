class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.insert(0, 0)
        heights.append(0)
        result = 0
        stack = list()
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                prev_idx = stack.pop()
                if stack:
                    result = max(result, heights[prev_idx] * (i - 1 - stack[-1]), )
            stack.append(i)
        return result
