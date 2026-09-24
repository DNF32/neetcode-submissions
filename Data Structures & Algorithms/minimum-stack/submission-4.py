class MinStack:

    def __init__(self):
        self.values = []
        self._minVal = 2**31 + 1
        self.minStack = [] 
        

    def push(self, val: int) -> None:
        if val < self._minVal:
            self._minVal = val
        self.values.append(val)
        self.minStack.append(self._minVal)

    def pop(self) -> None:
        self.values.pop(-1)
        self.minStack.pop(-1)
        if not self.minStack:
            self._minVal = 2**31 + 1
            return 
        self._minVal= self.minStack[-1]

    def top(self) -> int:
        return self.values[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        
