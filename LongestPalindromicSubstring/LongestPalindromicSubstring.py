class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) == 1:
            return s

        max_len = 0
        best_word = [0, 0]

        def expand(left, right):
            while s[left] == s[right]:
                left -= 1
                right += 1
                if left < 0 or right == len(s):
                    break
            left += 1
            right -= 1
            return left, right

        for i in range(len(s) - 1):
            odd = expand(i, i)
            even = expand(i, i+1)

            if (odd[1] - odd[0] + 1) > max_len:
                max_len = odd[1] - odd[0] + 1
                best_word = (odd[0], odd[1])
            if (even[1] - even[0] + 1) > max_len:
                max_len = even[1] - even[0] + 1
                best_word = (even[0], even[1])
        
        return s[best_word[0]:best_word[1]+1]

solution = Solution()
# ans = solution.longestPalindrome("babad"); assert ans == "aba", ans
# ans = solution.longestPalindrome("cbbd"); assert ans == "bb", ans
# ans = solution.longestPalindrome("ac"); assert ans == "a", ans
ans = solution.longestPalindrome("bb"); assert ans == "bb", ans
