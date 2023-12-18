class Solution:
    def productExceptSelf(self, nums):
        left_prod = 1
        right_prod = 1
        res = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            res[i] *= left_prod
            left_prod *= nums[i]
            res[-(i+1)] *= right_prod
            right_prod *= nums[-(i+1)]
        return res

solution = Solution()
ans = solution.productExceptSelf([1,2,3,4]); assert ans == [24,12,8,6], ans
ans = solution.productExceptSelf([-1,1,0,-3,3]); assert ans == [0,0,9,0,0], ans
