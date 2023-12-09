class Solution:
    def majorityElement(self, nums) -> int:
        # Moore voting algorithm
        elem = nums[0]
        count = 0
        for num in nums:
            if num == elem:
                count += 1
            else:
                count -= 1
            
            if count == 0:
                elem = num
                count = 1
        return elem

solution = Solution()
ans = solution.majorityElement([3,2,3]); assert ans == 3, ans
ans = solution.majorityElement([2,2,1,1,1,2,2]); assert ans == 2, ans
