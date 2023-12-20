class Solution:

    def combinationSum(self, candidates, target: int):
        # Use DFS to search all possible combinations
        self.res = []
        def dfs(candidates, target, combi, ind):
            if target < 0:
                return
            elif target == 0:
                self.res.append(combi)
                return
            else:
                for i in range(ind, len(candidates)):
                    num = candidates[i]
                    dfs(candidates, target-num, combi + [num], i)
        dfs(candidates, target, [], 0)

        return self.res


solution = Solution()
ans = solution.combinationSum([2,3,6,7], 7); assert ans == [[2,2,3],[7]], ans
ans = solution.combinationSum([2,3,5], 8); assert ans == [[2,2,2,2],[2,3,3],[3,5]], ans
ans = solution.combinationSum([2], 1); assert ans == [], ans
