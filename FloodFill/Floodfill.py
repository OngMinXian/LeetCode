class Solution:
    def floodFill(self, image, sr: int, sc: int, color: int):
        def dfs(row, col, scolor):
            # Check valid row and col
            if 0 <= row < len(image) and 0 <= col < len(image[0]):
                # Check if connected
                if image[row][col] == scolor:
                    image[row][col] = color

                    dfs(row+1, col, scolor)
                    dfs(row-1, col, scolor)
                    dfs(row, col+1, scolor)
                    dfs(row, col-1, scolor)

        # Edge case
        if color == image[sr][sc]:
            return image

        dfs(sr, sc, image[sr][sc])

        return image

solution = Solution()
ans = solution.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2); assert ans == [[2,2,2],[2,2,0],[2,0,1]], ans
ans = solution.floodFill([[0,0,0],[0,0,0]], 0, 0, 0); assert ans == [[0,0,0],[0,0,0]], ans
