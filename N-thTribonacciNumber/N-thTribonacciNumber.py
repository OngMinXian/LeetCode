class Solution:
    def tribonacci(self, n: int) -> int:
        # Edge cases:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1

        t0, t1, t2 = 0, 1, 1
        for i in range(3, n + 1):
            t0, t1, t2 = t1, t2, (t0 + t1 + t2)
        return t2

solution = Solution()
ans = solution.tribonacci(4); assert ans == 4, ans
ans = solution.tribonacci(25); assert ans == 1389537, ans