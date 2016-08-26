import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        heap = []
        for r in xrange(len(matrix)):
            for c in xrange(len(matrix[0])):
                if len(heap) < k:
                    heapq.heappush(heap, -matrix[r][c])
                elif -heap[0] > matrix[r][c]:
                    heapq.heappush(heap, -matrix[r][c])
                    heapq.heappop(heap)
        return -heap[0]
                    
