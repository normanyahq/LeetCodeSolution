class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        s1, s2, s3 = 0, -prices[0], float('-inf')
        for i in xrange(1, len(prices)):
            t_s1 = max(s1, s3)
            t_s2 = max(s2, s1-prices[i])
            t_s3 = s2 + prices[i]
            s1, s2, s3 = t_s1, t_s2, t_s3
        return max(s1, s3)
