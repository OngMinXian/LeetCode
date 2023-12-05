class Solution:
    def reverseVowels(self, s: str) -> str:
        # Use pointers for front and end
        s = list(s)
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O' ,'U'}
        left = 0
        right = len(s) - 1
        while left < right:
            # Both sides encountered vowel
            if s[left] in vowels and s[right] in vowels:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

            # Only left/right side encountered vowel
            elif s[left] in vowels:
                right -= 1
            elif s[right] in vowels:
                left += 1

            # Both not vowels
            else:
                left += 1
                right -= 1

        return ''.join(s)

solution = Solution()
ans = solution.reverseVowels('hello'); assert ans == 'holle', ans
ans = solution.reverseVowels('leetcode'); assert ans == 'leotcede', ans
