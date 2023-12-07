class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        # Minimum cost to reach stair n depends on minimum cost of n-1 and n-2, use 1D dynamic programming
        dp = [0 for i in range(len(cost)+ 1 )]
        for i in range(2, len(cost) + 1):
            dp[i] = min(dp[i - 2] + cost[i - 2], dp[i - 1] + cost[i - 1])

        return dp[-1]

solution = Solution()
ans = solution.minCostClimbingStairs([10,15,20]); assert ans == 15, ans
ans = solution.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]); assert ans == 6, ans
