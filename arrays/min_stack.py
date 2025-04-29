class MinStack:
    """
    Min stack that would do push pop getmin in O(1) time

    Trick: min_stack[i] = smallest value in the stack from i = index_of_value_min_stack[i]...n
    Alternative: use pair (val, i) where i is the index of last minimum index on the left
    Time Complexity: O(1)
    """
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]: # <= not <, record duplicating min value
            self.min_stack.append(val)

    def pop(self) -> None:
        v = self.stack.pop()
        if v == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()