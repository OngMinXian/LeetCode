class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = {}
        for char in s:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
        
        res = 0
        has_odd = False
        for count in counts.values():
            # odd case
            if count % 2:
                has_odd = True
                res += count - 1
            # even case
            else:
                res += count

        return res + 1 if has_odd else res
        
solution = Solution()
ans = solution.longestPalindrome('abccccdd'); assert ans == 7, ans
ans = solution.longestPalindrome('a'); assert ans == 1, ans
