class MinStack:

    def __init__(self):
        # for each element of the stack[i], the element at minstack[i], is the current min for stack[i - n...]
        # (meaning everything below it)
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # if there is already minstack, append with either ANOTHER instance of the existing number on top of the stack,
        # or the new val, whatever is lower
        if self.minstack:
            self.minstack.append(min(val, self.minstack[-1]))
        else:
            self.minstack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # return min(self.stack)
        # This is not and O(1) operation, which is why we have to add the minstack logic at init and push
        return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()