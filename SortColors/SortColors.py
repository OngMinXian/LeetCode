class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        curr_ind = 0
        left_ind = 0
        right_ind = len(nums) - 1
        while curr_ind <= right_ind:
            if nums[curr_ind] == 0:
                nums[left_ind], nums[curr_ind] = nums[curr_ind], nums[left_ind]
                left_ind += 1
                curr_ind += 1
            elif nums[curr_ind] == 2:
                nums[right_ind], nums[curr_ind] = nums[curr_ind], nums[right_ind]
                right_ind -= 1
            elif nums[curr_ind] == 1:
                curr_ind += 1
        return nums

solution = Solution()
ans = solution.sortColors([2,0,2,1,1,0]); assert ans == [0,0,1,1,2,2], ans
ans = solution.sortColors([2,0,1]); assert ans == [0,1,2], ans
