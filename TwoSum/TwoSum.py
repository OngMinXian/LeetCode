class Solution:
    def twoSum(self, nums, target: int):
        # Use hash table
        hash_table = {}
        for i in range(len(nums)):
            if target - nums[i] in hash_table:
                return [i, hash_table[target - nums[i]]]
            else:
                hash_table[nums[i]] = i

solution = Solution()
ans = solution.twoSum([2,7,11,15], 9); assert ans == [0,1], ans
ans = solution.twoSum([3,2,4], 6); assert ans == [1,2], ans
ans = solution.twoSum([3,3], 6); assert ans == [0,1], ans
