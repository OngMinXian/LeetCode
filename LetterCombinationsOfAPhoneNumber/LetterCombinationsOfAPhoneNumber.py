class Solution:
    def letterCombinations(self, digits: str):
        mapping = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        
        def dfs(digits, solution):
            if digits == '':
                return solution
            else:
                digit = digits[0]
                letters = mapping[digit]
                if solution == []:
                    for letter in letters:
                        solution.append(letter)
                else:
                    new_lst = []
                    for i in solution:
                        for letter in letters:
                            new_lst.append(i + letter)
                    solution = new_lst
                return dfs(digits[1:], solution)

        return dfs(digits, [])

solution = Solution()
ans = solution.letterCombinations('23'); assert ans == ["ad","ae","af","bd","be","bf","cd","ce","cf"], ans
ans = solution.letterCombinations(''); assert ans == [], ans
ans = solution.letterCombinations('2'); assert ans == ["a","b","c"], ans
