class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_table = {}
        for char in ransomNote:
            if char in hash_table:
                hash_table[char] += 1
            else:
                hash_table[char] = 1

        for char in magazine:
            if char in hash_table:
                hash_table[char] -= 1

        for counts in hash_table.values():
            if counts > 0:
                return False
            
        return True
    
solution = Solution()
ans = solution.canConstruct('a', 'b'); assert ans == False, ans
ans = solution.canConstruct('aa', 'ab'); assert ans == False, ans
ans = solution.canConstruct('aa', 'aab'); assert ans == True, ans
