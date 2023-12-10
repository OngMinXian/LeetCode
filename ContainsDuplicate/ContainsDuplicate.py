class Solution:
    def containsDuplicate(self, nums):
        hash_map = {}
        for num in nums:
            if num in hash_map:
                return True
            else:
                hash_map[num] = True
        return False

solution = Solution()
ans = solution.containsDuplicate([1,2,3,1]); assert ans == True, ans
ans = solution.containsDuplicate([1,2,3,4]); assert ans == False, ans
ans = solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2]); assert ans == True, ans
