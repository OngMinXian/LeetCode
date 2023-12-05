class Solution:
    def largestAltitude(self, gain) -> int:
        curr_alt = 0
        highest_alt = 0
        for i in gain:
            curr_alt += i
            if curr_alt > highest_alt:
                highest_alt = curr_alt
        return highest_alt

solution = Solution()
ans = solution.largestAltitude([-5, 1, 5, 0, -7]); assert ans == 1, ans
ans = solution.largestAltitude([-4, -3, -2, -1, 4, 3, 2]); assert ans == 0, ans
