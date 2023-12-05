class Solution:
    def findDifference(self, nums1, nums2):
        # Use Python sets
        set1 = set(nums1)
        set2 = set(nums2)
        return [list(set1 - set2), list(set2 - set1)]
 
solution = Solution()
ans = solution.findDifference([1,2,3], [2,4,6]); assert ans == [[1,3],[4,6]], ans
ans = solution.findDifference([1,2,3,3], [1,1,2,2]); assert ans == [[3],[]], ans
