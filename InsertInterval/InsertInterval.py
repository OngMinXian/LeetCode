class Solution:
    def insert(self, intervals, newInterval):
        pass

solution = Solution()
ans = solution.insert([[1,3],[6,9]], [2,5]); assert ans == [[1,5],[6,9]], ans
ans = solution.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]); assert ans == [[1,2],[3,10],[12,16]], ans
