# Min Stack
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# Implement the MinStack class:
# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.

class MinStack:

    def __init__(self):
        self.minstk = []
        self.stk = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        if len(self.minstk) == 0 or val < self.getMin():
            self.minstk.append(val)
        else:
            self.minstk.append(self.getMin())

    def pop(self) -> None:
        res = self.stk.pop()
        self.minstk.pop()
        return res

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.minstk[-1]
