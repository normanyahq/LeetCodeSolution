class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        answer = 0
        while n:
            answer += n / 5
            n /= 5
        return answer
