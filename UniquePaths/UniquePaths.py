class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for j in range(n)] for i in range(m)]
        for j in range(n):
            dp[0][j] = 1
        for i in range(1, m):
            for j in range(n):
                if i-1 >= 0:
                    dp[i][j] = dp[i-1][j]
                if j-1 >= 0:
                    dp[i][j] += dp[i][j-1]
        return dp[-1][-1]

solution = Solution()
ans = solution.uniquePaths(3, 7); assert ans == 28, ans
ans = solution.uniquePaths(3, 2); assert ans == 3, ans
