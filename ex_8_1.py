class MaxStack:

    def __init__(self):
        self.max = None
        self.stack = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.max is None:
            self.max = x
        elif x > self.max:
            self.max = x    

    def pop(self) -> None:
        x = self.stack.pop()
        if x == self.max:
            if len(self.stack) == 0:
                self.max = None
            else:
                self.max = max(self.stack)

    def top(self) -> int:
        return self.stack[-1]

    def getMax(self) -> int:
        return self.max

