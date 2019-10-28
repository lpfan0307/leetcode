class Solution(object):
    def maxProfit(self, prices):
        s = 0
        for i in range(len(prices)-1):
            s += max(0, prices[i+1]-prices[i])
        return s