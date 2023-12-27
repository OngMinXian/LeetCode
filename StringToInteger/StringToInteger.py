class Solution:
    def myAtoi(self, s: str) -> int:
        is_positive = True
        start_num = False
        num = ''
        for char in s:
            # Ignore leading white spaces
            if char == ' ' and not start_num:
                continue
            
            # Encounter + or - sign
            if char == '+' and not start_num:
                is_positive = True
                start_num = True
                continue
            elif char == '-' and not start_num:
                is_positive = False
                start_num = True
                continue

            # Break if not numeric
            if not char.isnumeric():
                break

            # Encounter numeric without + or - sign
            if not start_num and char.isnumeric():
                start_num = True
                num += char
                continue

            # Encounter numeric after start char
            if start_num and char.isnumeric():
                num += char

        if num == '':
            return 0
        num = int(num) if is_positive else -int(num)
        if num > 2**31 - 1:
            return 2**31 - 1
        if num < -2**31:
            return -2**31
        return num

solution = Solution()
ans = solution.myAtoi("42"); assert ans == 42, ans
ans = solution.myAtoi("   -42"); assert ans == -42, ans
ans = solution.myAtoi("4193 with words"); assert ans == 4193, ans
ans = solution.myAtoi("words and 987"); assert ans == 0, ans
ans = solution.myAtoi("+-12"); assert ans == 0, ans
ans = solution.myAtoi("   +0 123"); assert ans == 0, ans
