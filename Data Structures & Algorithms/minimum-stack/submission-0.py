class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        min_so_far = self.stack[0]
        for num in self.stack:
            if num < min_so_far:
                min_so_far = num
        return min_so_far
        
