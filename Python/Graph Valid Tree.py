"""
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

For example:

Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.

Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.

Hint:

Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], what should your return? Is this case a valid tree?
According to the definition of tree on Wikipedia: “a tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.”
"""

# BFS
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges) != n - 1: return False
        
        neighbors, visit_from = {}, {}
        for i in range(n):
            visit_from[i] = -1
            neighbors[i] = []
        for edge in edges:
            neighbors[edge[0]].append(edge[1])
            neighbors[edge[1]].append(edge[0])
        
        # BFS
        visited = {}
        q = collections.deque()
        q.append(0)
        while q:
            i = q.popleft()
            visited[i] = True
            for node in neighbors[i]:
                if visit_from[i] != node:
                    if node in visited:
                        return False
                    else:
                        visited[node] = True
                        visit_from[node] = i
                        q.append(node)
        return len(visited) == n

# DFS
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        neighbors = {i: [] for i in range(n)}
        for v, w in edges:
            neighbors[v] += w,
            neighbors[w] += v,
        def visit(v):
            map(visit, neighbors.pop(v, []))
        visit(0)
        return len(edges) == n-1 and not neighbors
