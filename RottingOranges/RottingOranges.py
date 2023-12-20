class Solution:
    def orangesRotting(self, grid) -> int:
        # Initialize BFS queue, current time, number of fresh oranges and rotten sources
        queue = []
        curr_time = 0
        no_fresh = 0
        curr_rotten = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    curr_rotten.append((i, j))
                if grid[i][j] == 1:
                    no_fresh += 1
        queue.append(curr_rotten)

        # Edge case
        if no_fresh == 0:
            return 0

        # Carries out mutli-source BFS
        while queue and no_fresh:
            curr_rotten = queue.pop(0)
            new_rotten = []
            for source in curr_rotten:
                i, j = source
                if 0 <= i - 1 and grid[i - 1][j] == 1:
                    new_rotten.append((i - 1, j))
                    grid[i - 1][j] = 2
                    no_fresh -= 1

                if i + 1 < len(grid) and grid[i + 1][j] == 1:
                    new_rotten.append((i + 1, j))
                    grid[i + 1][j] = 2
                    no_fresh -= 1

                if 0 <= j - 1 and grid[i][j - 1] == 1:
                    new_rotten.append((i, j - 1))
                    grid[i][j - 1] = 2
                    no_fresh -= 1

                if j + 1 < len(grid[0]) and grid[i][j + 1] == 1:
                    new_rotten.append((i, j + 1))
                    grid[i][j + 1] = 2
                    no_fresh -= 1

            if new_rotten:
                queue.append(new_rotten)
            curr_time += 1

        return curr_time if no_fresh == 0 else -1

solution = Solution()
ans = solution.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]); assert ans == 4, ans
ans = solution.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]); assert ans == -1, ans
ans = solution.orangesRotting([[0,2]]); assert ans == 0, ans
ans = solution.orangesRotting([[1],[2]]); assert ans == 1, ans
