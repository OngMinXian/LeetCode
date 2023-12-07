class Solution:
    def singleNumber(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]
        
        # Use XOR
        res = 0
        for i in nums:
            res ^= i

        return res

solution = Solution()
ans = solution.singleNumber([2,2,1]); assert ans == 1, ans
ans = solution.singleNumber([4,1,2,1,2]); assert ans == 4, ans
ans = solution.singleNumber([1]); assert ans == 1, ans
