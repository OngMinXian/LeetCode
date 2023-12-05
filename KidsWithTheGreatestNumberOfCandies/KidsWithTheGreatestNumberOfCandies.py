class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        
        curr_highest = max(candies)
        res = []
        for kid in candies:
            if kid + extraCandies >= curr_highest:
                res.append(True)
            else:
                res.append(False)
        return res

solution = Solution()
assert solution.kidsWithCandies([2, 3, 5, 1, 3], 3) == [True, True, True, False, True]
assert solution.kidsWithCandies([4, 2, 1, 1, 2], 1) == [True, False, False, False, False]
assert solution.kidsWithCandies([12, 1, 12], 3) == [True, False, True]

