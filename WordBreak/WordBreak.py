class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(len(s) + 1):
            for j in range(i):
                substr = s[j:i]
                if dp[j] and substr in wordDict:
                    dp[i] = True
        return dp[-1]

solution = Solution()
ans = solution.wordBreak("leetcode", ["leet","code"]); assert ans == True, ans
ans = solution.wordBreak("applepenapple", ["apple","pen"]); assert ans == True, ans
ans = solution.wordBreak("catsandog", ["cats","dog","sand","and","cat"]); assert ans == False, ans
ans = solution.wordBreak("abcd", ["a","abc","b","cd"]); assert ans == True, ans
ans = solution.wordBreak("aaaaaaa", ["aaaa","aa"]); assert ans == False, ans
