class Solution:
    def maxSubArray(self, nums) -> int:
        # DP approach to find max sum ending at ith char without using a DP table
        max_sum = nums[0]
        max_sum_to_i = nums[0]
        for i in range(1, len(nums)):
            max_sum_to_i = max(max_sum_to_i + nums[i], nums[i])
            max_sum = max(max_sum, max_sum_to_i)
        return max_sum

solution = Solution()
ans = solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]); assert ans == 6, ans
ans = solution.maxSubArray([1]); assert ans == 1, ans
ans = solution.maxSubArray([5,4,-1,7,8]); assert ans == 23, ans
