from collections import deque

class Solution:
    def updateMatrix(self, mat):

        m, n = len(mat), len(mat[0])
        max_value = m + n + 1
        queue = deque()
        res = [[max_value for j in range(n)] for i in range(m)]

        # Initialize BFS
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j, 0))

        # BFS
        while queue:
            i, j, dist = queue.popleft()
            if 0 <= i < m and 0 <= j < n and res[i][j] == max_value:
                res[i][j] = dist
                queue.append((i + 1, j, dist + 1))
                queue.append((i - 1, j, dist + 1))
                queue.append((i, j + 1, dist + 1))
                queue.append((i, j - 1, dist + 1))
        
        return res
    
solution = Solution()
ans = solution.updateMatrix([[0,0,0],[0,1,0],[0,0,0]]); assert ans == [[0,0,0],[0,1,0],[0,0,0]], ans
ans = solution.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]); assert ans == [[0,0,0],[0,1,0],[1,2,1]], ans
