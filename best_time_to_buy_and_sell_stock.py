
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<=1:
            return 0
        res = prices[1] - prices[0]
        min_price = prices[0]
        for i in range(2,len(prices)):
            min_price = min(prices[i-1],min_price)
            current_profit  = prices[i]-min_price
            if res<current_profit:
                res = current_profit
        if res<0:
            return 0
        return res
