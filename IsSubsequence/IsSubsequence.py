class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # 2 pointers, 1 for each string
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        
        return i == len(s)

solution = Solution()
ans = solution.isSubsequence('abc', 'ahbgdc'); assert ans == True, ans
ans = solution.isSubsequence('axc', 'ahbgdc'); assert ans == False, ans
