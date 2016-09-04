class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        row = len(matrix)
        col = len(matrix[0])
        left = 0
        right = row * col - 1
        R = lambda x: x//col
        C = lambda x: x % col
        while left <= right:
            mid = (left + right) / 2
            if matrix[R(mid)][C(mid)] == target:
                return True
            elif matrix[R(mid)][C(mid)] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False
