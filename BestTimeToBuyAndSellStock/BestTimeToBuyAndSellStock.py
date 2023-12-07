class Solution:
    def maxProfit(self, prices) -> int:
        min_price = prices[0]
        max_profit = 0
        for i in prices:
            if i - min_price > max_profit:
                max_profit = i - min_price
            if min_price > i:
                min_price = i

        return max_profit

solution = Solution()
ans = solution.maxProfit([7,1,5,3,6,4]); assert ans == 5, ans
ans = solution.maxProfit([7,6,4,3,1]); assert ans == 0, ans
