class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        s = sum(A)
        cur_sum = sum([i * v for i, v in enumerate(A)])
        result = cur_sum
        for i in range(1, len(A)):
            cur_sum += s - len(A) * (A[len(A)-i])
            result = max(cur_sum, result)
        return result
        
