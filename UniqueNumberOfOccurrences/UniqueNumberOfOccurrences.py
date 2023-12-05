class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        # Get occurances in hash
        hash = {}
        for i in arr:
            hash[i] = hash.get(i, 0) + 1

        # Check uniqueness
        return len(set(hash.values())) == len(hash)
    
solution = Solution()
ans = solution.uniqueOccurrences([1,2,2,1,1,3]); assert ans == True, ans
ans = solution.uniqueOccurrences([1,2]); assert ans == False, ans
ans = solution.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]); assert ans == True, ans
