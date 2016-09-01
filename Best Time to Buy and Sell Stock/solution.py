class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        result = 0
        min_price = prices[0]
        for i in prices:
            result = max(i - min_price, result)
            min_price = min(i, min_price)
        return result
        
