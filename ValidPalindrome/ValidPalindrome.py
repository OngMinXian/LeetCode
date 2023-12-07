class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            left_char, right_char = s[left].lower(), s[right].lower()
            if not left_char.isalnum():
                left += 1

            elif not right_char.isalnum():
                right -= 1

            elif left_char == right_char:
                left += 1
                right -= 1

            elif left_char != right_char:
                return False
        return True

solution = Solution()
ans = solution.isPalindrome("A man, a plan, a canal: Panama"); assert ans == True, ans
ans = solution.isPalindrome("raceacar"); assert ans == False, ans
ans = solution.isPalindrome(" "); assert ans == True, ans
