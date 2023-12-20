class Solution:
    def numIslands(self, grid) -> int:

        def bfs_convert(row_source, col_source):
            if grid[row_source][col_source] == "1":
                grid[row_source][col_source] = "0"
            else:
                return
            
            if 0 <= row_source - 1:
                bfs_convert(row_source - 1, col_source)
            if row_source + 1 < len(grid):
                bfs_convert(row_source + 1, col_source)
            if 0 <= col_source - 1:
                bfs_convert(row_source, col_source - 1)
            if col_source + 1 < len(grid[0]):
                bfs_convert(row_source, col_source + 1)

        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    count += 1
                    bfs_convert(row, col)

        return count

solution = Solution()
ans = solution.numIslands([
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]); assert ans == 1, ans
ans = solution.numIslands([
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]); assert ans == 3, ans
