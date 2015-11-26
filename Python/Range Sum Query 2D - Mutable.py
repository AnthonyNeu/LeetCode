"""
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
update(3, 2, 2)
sumRegion(2, 1, 4, 3) -> 10
Note:
The matrix is only modifiable by the update function.
You may assume the number of calls to update and sumRegion function is distributed evenly.
You may assume that row1 ≤ row2 and col1 ≤ col2.
"""

# using 2D binary indexed tree
# O(log m * log n) per query/update
class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if not matrix:
            self.m, self.n = 0, 0
            return
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.matrix = [[0 for _ in range(self.n)] for _ in range(self.m)]
        self.tree = [[0 for _ in range(self.n + 1)] for _ in range(self.m + 1)]
        for i in range(self.m):
            for j in range(self.n):
                self.update(i, j, matrix[i][j])

    def update(self, row, col, val):
        """
        update the element at matrix[row,col] to val.
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        if self.m == 0 or self.n == 0:
            return
        delta = val - self.matrix[row][col]
        self.matrix[row][col] = val
        i = row + 1
        while i <= self.m:
            j = col + 1
            while j <= self.n:
                self.tree[i][j] += delta
                j += j &(-j)
            i += i & (-i)

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if self.m == 0 or self.n == 0:
            return 0
        return self._sum(row2 + 1, col2 + 1) + self._sum(row1, col1) - self._sum(row1, col2 + 1) - self._sum(row2 + 1, col1)
    
    def _sum(self, row, col):
        result = 0
        i = row
        while i > 0:
            j = col
            while j > 0:
                result += self.tree[i][j]
                j -= j &(-j)
            i -= i & (-i)
        return result

# using 2D segment tree
# O(log (m * n)) per query/update
class QuadTreeNode:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.mid_x = x1 + (x2 - x1) / 2
        self.mid_y = y1 + (y2 - y1) / 2
        self.sum = 0
        self.ul = None
        self.ur = None
        self.bl = None
        self.br = None

class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        if not matrix:
            return
        self.root = self._build(0, 0, len(matrix) - 1, len(matrix[0]) - 1)
        
    def _build(self, x1, y1, x2, y2):
        root = QuadTreeNode(x1, y1, x2, y2)
        if x1 == x2 and y1 == y2:
            root.sum = self.matrix[x1][y1]
        else:
            mid_x = x1 + (x2 - x1) / 2
            mid_y = y1 + (y2 - y1) / 2
            root.ul = self._build(x1, y1, mid_x, mid_y)
            root.sum += root.ul.sum
            if mid_y + 1 <= y2:
                root.ur = self._build(x1, mid_y + 1, mid_x, y2)
                root.sum += root.ur.sum
            if mid_x + 1 <= x2:
                root.bl = self._build(mid_x + 1, y1, x2, mid_y)
                root.sum += root.bl.sum
            if mid_x + 1 <= x2 and mid_y + 1 <= y2:
                root.br = self._build(mid_x + 1, mid_y + 1, x2, y2)
                root.sum += root.br.sum
        return root
    
    def _update(self, root, row, col, val):
        if root.x1 > row or root.x2 < row or root.y1 > col or root.y2 < col:
            return
        if root.x1 == root.x2 and root.x1 == row and root.y1 == root.y2 and root.y1 == col:
            root.sum = val
        else:
            root.sum = 0
            if row <= root.mid_x and col <= root.mid_y:
                self._update(root.ul, row, col, val)
                root.sum += root.ul.sum
            elif row <= root.mid_x and col > root.mid_y:
                self._update(root.ur, row, col, val)
                root.sum += root.ur.sum
            elif row > root.mid_x and col <= root.mid_y:
                self._update(root.bl, row, col, val)
                root.sum += root.bl.sum
            else:
                self._update(root.br, row, col, val)
                root.sum += root.br.sum
    
    def _query(self, root, row1, col1, row2, col2):
        if not root:
            return 0
        if root.x1 >= row1 and root.y1 <= col1 and root.x2 >= row2 and root.y2 <= col2:
            return root.sum
        result = 0
        if row1 <= root.mid_x and col1 <= root.mid_y:
            result += self._query(root.ul, row1, col1, row2, col2)
        if row1 <= root.mid_x and col2 > root.mid_y:
            result += self._query(root.ur, row1, col1, row2, col2)
        if row2 > root.mid_x and col1 <= root.mid_y:
            result += self._query(root.bl, row1, col1, row2, col2)
        if row2 > root.mid_x and col2 > root.mid_y:
            result += self._query(root.br, row1, col1, row2, col2)
        return result

    def update(self, row, col, val):
        """
        update the element at matrix[row,col] to val.
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        if not self.matrix:
            return
        self._update(self.root, row, col, val)

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if not self.matrix:
            return 0
        return self._query(self.root, row1, col1, row2, col2)

# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.update(1, 1, 10)
# numMatrix.sumRegion(1, 2, 3, 4)
