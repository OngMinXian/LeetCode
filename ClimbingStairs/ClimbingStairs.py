class Solution:
    def climbStairs(self, n: int) -> int:
        # Number of ways is dependant on previous results
        ways = []
        for i in range(n):
            if i == 0:
                ways.append(1)
            elif i == 1:
                ways.append(2)
            else:
                ways.append(ways[i-1] + ways[i-2])
        return ways[-1]
        
solution = Solution()
ans = solution.climbStairs(2); assert ans == 2, ans
ans = solution.climbStairs(3); assert ans == 3, ans
