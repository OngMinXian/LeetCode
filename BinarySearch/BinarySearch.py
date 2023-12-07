class Solution:
    def search(self, nums, target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            # Found target
            if nums[mid] == target:
                return mid

            # Target is smaller
            if nums[mid] > target:
                high = mid - 1

            # Target is larger
            elif nums[mid] < target:
                low = mid + 1

        return -1

solution = Solution()
ans = solution.search([-1,0,3,5,9,12], 9); assert ans == 4, ans
ans = solution.search([-1,0,3,5,9,12], 2); assert ans == -1, ans
ans = solution.search([2], 2); assert ans == -0, ans
ans = solution.search([], 2); assert ans == -1, ans
