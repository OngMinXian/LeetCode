class MyQueue:

    def __init__(self):
        self.front_stack = []
        self.back_stack = []

    def push(self, x: int) -> None:
        self.front_stack.append(x)

    def pop(self) -> int:
        if not self.back_stack:
            while self.front_stack:
                self.back_stack.append(self.front_stack.pop(-1))
        return self.back_stack.pop(-1)

    def peek(self) -> int:
        if not self.back_stack:
            while self.front_stack:
                self.back_stack.append(self.front_stack.pop(-1))
        return self.back_stack[-1]

    def empty(self) -> bool:
        return not self.front_stack and not self.back_stack
