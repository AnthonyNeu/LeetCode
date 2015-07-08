"""
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Notes:
You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
"""

class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.s = []
        self.front = None

    # @param x, an integer
    # @return nothing
    def push(self, x):
        if self.empty():
            self.front = x
        self.s.append(x)
        
    # @return nothing
    def pop(self):
        cur = []
        for _ in xrange(len(self.s) - 1):
            cur.append(self.s[-1])
            self.front = cur[-1] 
            self.s.pop()
        self.s.pop()
        for _ in xrange(len(cur)):
            self.s.append(cur[-1])
            cur.pop()
        

    # @return an integer
    def peek(self):
        return self.front

    # @return an boolean
    def empty(self):
        return len(self.s) == 0