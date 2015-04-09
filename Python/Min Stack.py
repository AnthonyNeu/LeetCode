"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
"""


# O(n) Time
# O(1) Space
class MinStack:
    def __init__(self):
        self.min = None
        self.stack = []
        
    # @param x, an integer
    # @return an integer
    def push(self, x):
        if not self.stack:
            self.stack.append(0)
            self.min = x
        else:
            self.stack.append(x - self.min)
            if x < self.min:
                self.min = x

    # @return nothing
    def pop(self):
        x = self.stack.pop()
        if x < 0:
            self.min = self.min - x

    # @return an integer
    def top(self):
        x = self.stack[-1]
        if x > 0:
            return x + self.min
        else:
            return self.min
        
    # @return an integer
    def getMin(self):
        return self.min

#O(n) time
#O(n) space
class MinStack:
    def __init__(self):
        self.min = []
        self.stack = []
        
    # @param x, an integer
    # @return an integer
    def push(self, x):
        if not self.stack:
            self.stack.append(x)
            self.min.append(x) 
        else:
            self.stack.append(x)
            if x <= self.min[-1]:
                self.min.append(x)

    # @return nothing
    def pop(self):
        x = self.stack.pop()
        if x == self.min[-1]:
            self.min.pop()

    # @return an integer
    def top(self):
        return self.stack[-1]
        
    # @return an integer
    def getMin(self):
        return self.min[-1]