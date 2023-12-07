class Solution:
    def isValid(self, s: str) -> bool:
        # Use a stack
        stack = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                top_of_stack = stack.pop(-1)
                if {'(': ')', '[': ']', '{': '}'}[top_of_stack] != i:
                    return False
                
        return len(stack) == 0

solution = Solution()
ans = solution.isValid("()"); assert ans == True, ans
ans = solution.isValid("()[]{}"); assert ans == True, ans
ans = solution.isValid("(]"); assert ans == False, ans
