class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_len = len(a)
        b_len = len(b)

        if a_len < b_len:
            a = '0'*(b_len-a_len) + a
        elif b_len < a_len:
            b = '0'*(a_len-b_len) + b

        output = []
        carry_over = 0
        for i in range(1, max(a_len, b_len) + 1):
            add_tgt = int(a[-i]) + int(b[-i]) + carry_over
            if add_tgt == 0:
                output.append('0')
            elif add_tgt == 1:
                carry_over = 0
                output.append('1')
            elif add_tgt == 2:
                carry_over = 0
                output.append('0')
                carry_over = 1
            elif add_tgt == 3:
                output.append('1')
                carry_over = 1
        if carry_over:
            output.append('1')
        
        return ''.join(output[::-1])
        
solution = Solution()
ans = solution.addBinary('11', '1'); assert ans == '100', ans
ans = solution.addBinary('1010', '1011'); assert ans == '10101', ans
