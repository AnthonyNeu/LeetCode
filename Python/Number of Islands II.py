"""
A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example:

Given m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]].
Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).

0 0 0
0 0 0
0 0 0
Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.

1 0 0
0 0 0   Number of islands = 1
0 0 0
Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.

1 1 0
0 0 0   Number of islands = 1
0 0 0
Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.

1 1 0
0 0 1   Number of islands = 2
0 0 0
Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.

1 1 0
0 0 1   Number of islands = 3
0 1 0
We return the result as an array: [1, 1, 2, 3]
"""

class union_find:
    def __init__(self, m, n):
        self.father = {}
        self.m = m
        self.n = n
        for i in range(m):
            for j in range(n):
                id = self.convert_to_id(i, j)
                self.father[id] = id
    
    def find(self, x, y):
        parent = self.father[self.convert_to_id(x, y)]
        while parent != self.father[parent]:
            parent = self.father[parent]
        return parent
    
    def compressed_find(self, x, y):
        parent = self.father[self.convert_to_id(x, y)]
        while parent != self.father[parent]:
            parent = self.father[parent]
        # set all father to be parent we just get
        prev_father = self.father[self.convert_to_id(x, y)]
        while prev_father != self.father[prev_father]:
            prev_father, self.father[prev_father] = self.father[prev_father], parent
        return parent
    
    def union(self, x1, y1, x2, y2):
        f1 = self.find(x1, y1)
        f2 = self.find(x2, y2)
        if f1 != f2:
            self.father[f1] = f2
    
    def convert_to_id(self, x, y):
        return x * self.n + y

class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        if m == 0 or n == 0:
            return []
        if not positions or len(positions) == 0:
            return []
        island = [[False for _ in range(n)] for _ in range(m)]
        directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]
        count, uf, result = 0, union_find(m, n), []
        for position in positions:
            x, y = position[0], position[1]
            if not island[x][y]:
                count += 1
                island[x][y] = True
                for i in range(4):
                    nx, ny = x + directions[i][0], y + directions[i][1]
                    if 0 <= nx < m and 0 <= ny < n and island[nx][ny]:
                        position_father = uf.find(x, y)
                        now_father = uf.find(nx, ny)
                        if position_father != now_father:
                            count -= 1
                            uf.union(x, y, nx, ny)
            result.append(count)
        return result
