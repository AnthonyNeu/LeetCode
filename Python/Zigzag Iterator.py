"""
Given two 1d vectors, implement an iterator to return their elements alternately.

For example, given two 1d vectors:

v1 = [1, 2]
v2 = [3, 4, 5, 6]
By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1, 3, 2, 4, 5, 6].

Follow up: What if you are given k 1d vectors? How well can your code be extended to such cases?

Clarification for the follow up question - Update (2015-09-18):
The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases. If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic". For example, given the following input:

[1,2,3]
[4,5,6,7]
[8,9]
It should return [1,4,8,2,5,9,3,6,7].
"""

class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.vec = [v1, v2]
        self.y = 0
        self.max_length = max([len(x) for x in self.vec])
        if self.y != len(self.vec):
            self.x = 0
            self.findNextElement()
        

    def next(self):
        """
        :rtype: int
        """
        element = self.vec[self.y][self.x]
        self.y += 1
        self.findNextElement()
        return element
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.x < self.max_length
        
    def findNextElement(self):
        """
        :rtype: boo
        """
        while self.y != len(self.vec) and self.x >= len(self.vec[self.y]):
            self.y += 1
        
        if self.y == len(self.vec):
            self.y, self.x = 0, self.x + 1
            if self.x < self.max_length:
                self.findNextElement()
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())


class ZigzagIterator(object):

    def __init__(self, v1, v2):
        self.data = [(len(v), iter(v)) for v in (v1, v2) if v]

    def next(self):
        len, iter = self.data.pop(0)
        if len > 1:
            self.data.append((len-1, iter))
        return next(iter)

    def hasNext(self):
        return bool(self.data)
