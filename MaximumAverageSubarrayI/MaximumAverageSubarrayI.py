class Solution:
    def findMaxAverage(self, nums, k: int) -> float:
        # Simple sliding window problem
        running_sum = sum(nums[:k])
        max_avg = running_sum / k
        for i, num in enumerate(nums[k:]):
            running_sum = running_sum + num - nums[i]
            if running_sum / k > max_avg:
                max_avg = running_sum / k
        return max_avg

solution = Solution()
ans = solution.findMaxAverage([1, 12, -5, -6, 50, 3], 4); assert ans == 12.75, ans
ans = solution.findMaxAverage([5], 1); assert ans == 5.00, ans
