class MyQueue:
    """
    Implement queue using stacks
    
    Time Complexity: O(1) armotized
    Space Complexity: O(n)
    """

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self.peek() # make sure migrated to outstack
        return self.out_stack.pop() if self.out_stack else None

    def peek(self) -> int:
        if not self.out_stack: # migrate all instack to outstack if outstack rmpty
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()