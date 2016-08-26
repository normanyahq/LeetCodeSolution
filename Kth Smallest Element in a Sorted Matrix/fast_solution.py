import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        count = 0
        row = len(matrix)
        col = len(matrix[0])

        initial_r, initial_c = (0, 0) if k < row * col / 2 else (row-1, col-1)
        visited = set([(initial_r, initial_c)])
        sign = 1 if k < row * col / 2 else -1
        priority_queue = [(matrix[initial_r][initial_c] * sign, initial_r, initial_c)] # stores (row, col)
        k = row * col - k + 1 if k >= row * col / 2 else k
        while priority_queue:
            v, r, c = heapq.heappop(priority_queue)
            count += 1
            if count == k:
                return v * sign
            if r + sign < row and r + sign >= 0 and (r + sign, c) not in visited:
                heapq.heappush(priority_queue, (sign * matrix[r + sign][c], r + sign, c))
                visited.add((r + sign, c))
            if c + sign < col and c + sign >= 0 and (r, c + sign) not in visited:
                heapq.heappush(priority_queue, (sign * matrix[r][c + sign], r, c + sign))
                visited.add((r, c + sign))

        return 
                    
