class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = 0
        right = 0
        max_len = 0
        for i in range(len(s)):
            char = s[i]
            # Seen character and is part of current substring
            if char in seen and seen[char] >= left:
                left = seen[char] + 1
                
            # Have not seen character yet or not part of current substrng
            else:
                if max_len < right - left + 1:
                    max_len = right - left + 1
            
            # Move right pointer forward and record last seen index
            seen[char] = i
            right += 1
        return max_len

solution = Solution()
ans = solution.lengthOfLongestSubstring('abcabcbb'); assert ans == 3, ans
ans = solution.lengthOfLongestSubstring('bbbbb'); assert ans == 1, ans
ans = solution.lengthOfLongestSubstring('pwwkew'); assert ans == 3, ans
