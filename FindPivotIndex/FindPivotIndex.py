class Solution:
    def pivotIndex(self, nums) -> int:
        # Use 2 running sums, left and right of index sum
        ind = 0
        left_sum = 0
        right_sum = sum(nums) - nums[ind]
        while True:
            if left_sum == right_sum:
                return ind
            
            left_sum += nums[ind]
            ind += 1
            if ind == len(nums):
                break
            right_sum -= nums[ind]

        return -1
            

solution = Solution()
ans = solution.pivotIndex([1, 7, 3, 6, 5, 6]); assert ans == 3, ans
ans = solution.pivotIndex([1, 2, 3]); assert ans == -1, ans
ans = solution.pivotIndex([2, 1, -1]); assert ans == 0, ans
