class Solution:
    def countBits(self, n: int):
        # Base case
        res = [0, 1, 1]

        # Edge cases
        if n < 3:
            return res[:n + 1]

        for i in range(3, n + 1):
            # if even, same number of 1s as half its value
            if i % 2 == 0:
                res.append(res[i//2])
            
            # if odd, same number of 1s as half its (value - 1)
            else:
                res.append(res[i//2] + 1)

        return res

solution = Solution()
ans = solution.countBits(2); assert ans == [0,1,1], ans
ans = solution.countBits(5); assert ans == [0,1,1,2,1,2], ans
