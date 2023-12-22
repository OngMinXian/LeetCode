class Solution:
    def merge(self, intervals):
        intervals = sorted(intervals, key=lambda x: x[0])

        prev_start = None
        prev_end = None
        res = []
        for interval in intervals:
            if prev_start == None:
                prev_start = interval[0]
                prev_end = interval[1]
            else:
                if interval[0] <= prev_end:
                    prev_end = max(interval[1], prev_end)
                else:
                    res.append([prev_start, prev_end])
                    prev_start = interval[0]
                    prev_end = interval[1]

        res.append([prev_start, prev_end])
        return res

solution = Solution()
ans = solution.merge([[1,3],[2,6],[8,10],[15,18]]); assert ans == [[1,6],[8,10],[15,18]], ans
ans = solution.merge([[1,4],[4,5]]); assert ans == [[1,5]], ans
