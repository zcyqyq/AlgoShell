# Last updated: 2025/10/7 18:48:33
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [2**31 - 1] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i - coin] + 1, dp[i])
        if dp[-1] == 2**31 - 1:
            return -1
        else:
            return dp[-1]
        