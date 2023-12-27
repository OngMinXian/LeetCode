class Solution:
    def canPartition(self, nums) -> bool:
        total_sum = sum(nums)
        
        # Total sum must be even
        if total_sum % 2:
            return False
        
        # DP approach
        dp = [False] * (total_sum + 1)
        dp[0] = True
        # Include or do not include number
        for num in nums:
            for i in range(total_sum, -1, -1):
                if dp[i]:
                    dp[i + num] = True
        return dp[total_sum//2]

solution = Solution()
ans = solution.canPartition([1,5,11,5]); assert ans == True, ans
ans = solution.canPartition([1,2,3,5]); assert ans == False, ans
