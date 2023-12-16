class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                right_operand = stack.pop(-1)
                left_operand = stack.pop(-1)
                stack.append(left_operand + right_operand)
            elif token == '-':
                right_operand = stack.pop(-1)
                left_operand = stack.pop(-1)
                stack.append(left_operand - right_operand)
            elif token == '*':
                right_operand = stack.pop(-1)
                left_operand = stack.pop(-1)
                stack.append(left_operand * right_operand)
            elif token == '/':
                right_operand = stack.pop(-1)
                left_operand = stack.pop(-1)
                stack.append(int(left_operand / right_operand))
            else:
                stack.append(int(token))
        return stack[0]
    
solution = Solution()
ans = solution.evalRPN(["2","1","+","3","*"]); assert ans == 9, ans
ans = solution.evalRPN(["4","13","5","/","+"]); assert ans == 6, ans
ans = solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]); assert ans == 22, ans
