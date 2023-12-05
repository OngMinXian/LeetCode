class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        # Compare i and i+1 position, increment and decrement as required
        prev_plot = 0
        for plot in flowerbed:
            if prev_plot == 0 and plot == 0:
                n -= 1
                prev_plot = 1
            elif prev_plot == 0 and plot == 1:
                prev_plot = plot
            elif prev_plot == 1 and plot == 0:
                prev_plot = plot
            elif prev_plot == 1 and plot == 1:
                n += 1
                prev_plot = plot

        return n <= 0
        
solution = Solution()
ans = solution.canPlaceFlowers([1, 0, 0, 0, 1], 1); assert ans == True, ans
ans = solution.canPlaceFlowers([1, 0, 0, 0, 1], 2); assert ans == False, ans
ans = solution.canPlaceFlowers([0, 0, 1, 0, 1], 1); assert ans == True, ans
