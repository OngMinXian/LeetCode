import math

class Solution:
    def coinChange(self, coins, amount: int) -> int:
        dp = [math.inf for i in range(amount + 1)]
        dp[0] = 0
        for i in range(amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        if dp[-1] == math.inf:
            return -1
        return dp[-1]

solution = Solution()
ans = solution.coinChange([1,2,5], 11); assert ans == 3, ans
ans = solution.coinChange([2], 3); assert ans == -1, ans
ans = solution.coinChange([1], 0); assert ans == 0, ans
