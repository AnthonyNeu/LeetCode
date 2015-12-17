"""
You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You are given a 2D grid of values 0, 1 or 2, where:

Each 0 marks an empty land which you can pass by freely.
Each 1 marks a building which you cannot pass through.
Each 2 marks an obstacle which you cannot pass through.
The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

For example, given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2):

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0
The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal. So return 7.

Note:
There will be at least one building. If it is not possible to build such house according to the above rules, return -1.
"""

from collections import deque

class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return -1
        m, n = len(grid), len(grid[0])
        # for the cumulative distance
        distance = [[0 for j in range(n)] for i in range(m)]
        # for the visited times
        count = [[0 for j in range(n)] for i in range(m)]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        def bfs(i, j, dist, now_count):
            result, found = float("inf"), False
            queue = deque([(i, j)])
            while queue:
                next_level = deque([])
                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        nx, ny = x + directions[k][0], y + directions[k][1]
                        if nx >= 0 and nx < m and ny >= 0 and ny < n and grid[nx][ny] == 0 and count[nx][ny] == now_count:
                            distance[nx][ny] += dist
                            count[nx][ny] += 1
                            result, found = min(result, distance[nx][ny]), True
                            next_level.append((nx, ny))
                queue = next_level
                dist += 1
            return result if found else -1
        min_distance, now_count = -1, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    min_distance = bfs(i, j, 1, now_count)
                    now_count += 1
        return min_distance
