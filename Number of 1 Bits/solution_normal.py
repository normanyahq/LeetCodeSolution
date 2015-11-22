class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        answer = 0
        while n:
            answer += n & 1
            n >>= 1
        return answer
