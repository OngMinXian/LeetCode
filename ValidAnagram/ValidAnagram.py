class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_counts = {}
        for char in s:
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1

        char_counts_2 = {}
        for char in t:
            if char in char_counts_2:
                char_counts_2[char] += 1
            else:
                char_counts_2[char] = 1

        for k, v in char_counts.items():
            if char_counts_2.get(k, 0) != v:
                return False
            
        for k, v in char_counts_2.items():
            if char_counts.get(k, 0) != v:
                return False
            
        return True

solution = Solution()
ans = solution.isAnagram('anagram', 'nagaram'); assert ans == True, ans
ans = solution.isAnagram('rat', 'car'); assert ans == False, ans
