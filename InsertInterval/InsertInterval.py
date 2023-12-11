class Solution:
    def insert(self, intervals, newInterval):

        new_start, new_end = newInterval
        left, right = [], []

        for interval in intervals:
            start, end = interval

            if start <= new_start <= end:
                new_start = start
            if start <= new_end <= end:
                new_end = end

            else:
                if new_start > end:
                    left.append(interval)
                
                elif start > new_end:
                    right.append(interval)

        return left + [[new_start, new_end]] + right

solution = Solution()
ans = solution.insert([[1,3],[6,9]], [2,5]); assert ans == [[1,5],[6,9]], ans
ans = solution.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]); assert ans == [[1,2],[3,10],[12,16]], ans
