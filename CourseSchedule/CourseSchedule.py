class Solution:
    def canFinish(self, numCourses, prerequisites) -> bool:
        # Build adjacency list and in degree
        adj_lst = {i: [] for i in range(numCourses)}
        inDegrees = [0] * numCourses
        for edge in prerequisites:
            v1, v2 = edge
            adj_lst[v2].append(v1)
            inDegrees[v1] += 1

        # Topo sort
        queue = []
        for v in range(numCourses):
            if inDegrees[v] == 0:
                queue.append(v)

        count = 0
        topoOrder = []
        while queue:
            curr_v = queue.pop(0)
            topoOrder.append(curr_v)
            count += 1

            for v in adj_lst[curr_v]:
                inDegrees[v] -= 1
                if inDegrees[v] == 0:
                    queue.append(v)

        return count == numCourses

solution = Solution()
ans = solution.canFinish(2, [[1,0]]); assert ans == True, ans
ans = solution.canFinish(2, [[1,0],[0,1]]); assert ans == False, ans
