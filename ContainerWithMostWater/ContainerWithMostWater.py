class Solution:
    def maxArea(self, height) -> int:
        left, right = 0, len(height) - 1
        max_area = min(height[left], height[right]) * (right - left)

        while left < right:
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
                
            curr_area = min(height[left], height[right]) * (right - left)
            if curr_area > max_area:
                max_area = curr_area

        return max_area


solution = Solution()
ans = solution.maxArea([1,8,6,2,5,4,8,3,7]); assert ans == 49, ans
ans = solution.maxArea([1,1]); assert ans == 1, ans
