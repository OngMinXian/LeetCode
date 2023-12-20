class Solution:
    def search(self, nums, target) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid

            # Left half sorted
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

            # Right half sorted
            if nums[mid] <= nums[high]:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1

solution = Solution()
ans = solution.search([4,5,6,7,0,1,2], 4); assert ans == 0, ans
ans = solution.search([4,5,6,7,0,1,2], 3); assert ans == -1, ans
ans = solution.search([1], 1); assert ans == 0, ans
ans = solution.search([1], 0); assert ans == -1, ans
