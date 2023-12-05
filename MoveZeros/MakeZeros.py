class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Handles edge case
        if len(nums) == 0 or len(nums) == 1:
            return
        
        # Use 2 pointers, 1 to keep track of most left zero and 1 to iterate through array
        non_zero_pointer, zero_pointer = 0, 0
        while non_zero_pointer < len(nums):
            
            if nums[non_zero_pointer] == 0:
                non_zero_pointer += 1
            else:
                if non_zero_pointer != zero_pointer:
                    nums[non_zero_pointer], nums[zero_pointer] = nums[zero_pointer], nums[non_zero_pointer]
                non_zero_pointer += 1
                zero_pointer += 1

solution = Solution()
nums = [0, 1, 0, 3, 12]; solution.moveZeroes(nums); assert nums == [1, 3, 12, 0, 0], nums
nums = [1, 0, 3, 12]; solution.moveZeroes(nums); assert nums == [1, 3, 12, 0], nums
nums = [0]; solution.moveZeroes(nums); assert nums == [0], nums
