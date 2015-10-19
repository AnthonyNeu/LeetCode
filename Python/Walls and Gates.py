"""
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

For example, given the 2D grid:
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:
  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
"""

class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    stack = [
                        (i + 1, j, 1),
                        (i - 1, j, 1),
                        (i, j + 1, 1),
                        (i, j - 1, 1)
                    ]
                    while stack:
                        ii, jj, dist = stack.pop()
                        if ii < 0 or ii >= len(rooms) or jj < 0 or jj >= len(rooms[0]) or rooms[ii][jj] < dist:
                            continue
                        rooms[ii][jj] = dist
                        stack.append((ii + 1, jj, dist + 1))
                        stack.append((ii - 1, jj, dist + 1))
                        stack.append((ii, jj + 1, dist + 1))
                        stack.append((ii, jj - 1, dist + 1))
