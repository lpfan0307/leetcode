class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = {}
        dp[0] = 0
       
        min_coin = coins[0]
        for coin in coins:
            dp[coin] = 1
            if min_coin > coin:
                min_coin = coin
        for i in range(min_coin+1, amount+1):
   
            min_count = amount + 1
            for coin in coins:
                
                if i-coin in dp:
                    if min_count >dp[i-coin] + 1:
                        min_count  = dp[i-coin] + 1
            if min_count!=amount+1:
                dp[i] = min_count
        if amount in dp:
            return dp[amount]
        return -1
coins = [1]
amount = 2
s = Solution()
print(s.coinChange(coins,amount))