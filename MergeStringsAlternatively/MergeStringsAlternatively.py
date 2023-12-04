class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        output = []

        # Find lengths
        len_word1 = len(word1)
        len_word2 = len(word2)

        # Concantenate string up to equal lengths
        len_shorter = min(len_word1, len_word2)
        for i in range(len_shorter):
            output.append(word1[i])
            output.append(word2[i])

        # Add remainder of string
        if len_word1 > len_word2:
            output.append(word1[len_shorter:])
        elif len_word1 < len_word2:
            output.append(word2[len_shorter:])

        return ''.join(output)
    
solution = Solution()
assert solution.mergeAlternately('abc', 'pqr') == 'apbqcr'
assert solution.mergeAlternately('ab', 'pqrs') == 'apbqrs'
assert solution.mergeAlternately('abcd', 'pq') == 'apbqcd'
