class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.min = float('inf')
        self.minStack.append(self.min)

    def push(self, val: int) -> None:
        self.min = min(val, self.min)
        self.stack.append(val)
        self.minStack.append(self.min)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        self.min = self.minStack[-1]   

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min        
