class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = 0
        right = 0
        max_len = 0
        for i in range(len(s)):
            char = s[i]
            if char not in seen:
                right += 1
            else:
                if max_len < right - left + 1:
                    max_len = right - left + 1
                left = seen[char] + 1
            seen[char] = i
        return max_len

solution = Solution()
# ans = solution.lengthOfLongestSubstring('abcabcbb'); assert ans == 3, ans
# ans = solution.lengthOfLongestSubstring('bbbbb'); assert ans == 1, ans
ans = solution.lengthOfLongestSubstring('pwwkew'); assert ans == 3, ans
