class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # There exists a gcd
        if str1 + str2 == str2 + str1:
            # Find gcd of lengths
            len_str1 = len(str1)
            len_str2 = len(str2)
            gcd = None
            for i in range(1, max(len_str1, len_str2)+1):
                if len_str1 % i == 0 and len_str2 % i == 0:
                    gcd = i
            return str1[:gcd]
        else:
            return ''


solution = Solution()
assert solution.gcdOfStrings('ABCABC', 'ABC') == 'ABC'
assert solution.gcdOfStrings('ABABAB', 'ABAB') == 'AB'
assert solution.gcdOfStrings('LEET', 'C0DE') == ''
assert solution.gcdOfStrings('AAAA', 'AA') == 'AA'

