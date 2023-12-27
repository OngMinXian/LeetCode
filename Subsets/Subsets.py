class Solution:
    def subsets(self, nums):
        def dfs(subset, choices, solution):
            for i in range(len(choices)):
                new_subset = subset.copy() + [choices[i]]
                solution.append(new_subset)
                dfs(new_subset, choices[i+1:], solution)

        solution = [[]]
        dfs([], nums, solution)
        return solution

solution = Solution()
ans = solution.subsets([1,2,3]); assert ans == [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]], ans
ans = solution.subsets([0]); assert ans == [[],[0]], ans
