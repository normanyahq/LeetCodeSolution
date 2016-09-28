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
    
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        heights = [1 if matrix[0][i] =="1" else 0 for i in range(len(matrix[0]))]
        print heights
        result = self.largestRectangleArea(list(heights))
        for r in range(1, len(matrix)):
            heights = [(heights[i] + 1) if matrix[r][i]=="1" else 0 for i in range(len(matrix[0]))]
            result = max(self.largestRectangleArea(list(heights)), result)
        return result
