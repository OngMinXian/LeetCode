class Solution:
    def permute(self, nums):
        def dfs(nums, combi, output):
            if nums == []:
                output.append(combi)
            else:
                for i in range(len(nums)):
                    dfs(nums[:i] + nums[i+1:], combi.copy() + [nums[i]], output)
        
        output = []
        dfs(nums, [], output)
        return output

solution = Solution()
ans = solution.permute([1,2,3]); assert ans == [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]], ans
ans = solution.permute([0,1]); assert ans == [[0,1],[1,0]], ans
ans = solution.permute([1]); assert ans == [[1]], ans
