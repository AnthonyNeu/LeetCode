"""
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

For example,
Given the following words in dictionary,

[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
The correct order is: "wertf".

Note:
You may assume all letters are in lowercase.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.
"""

#BFS
class Solution1(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        result, zero_in_degree_queue, in_degree, out_degree = "", collections.deque(), {}, {}
        nodes = sets.Set()
        
        for word in words:
            for char in word:
                if char not in nodes:
                    nodes.add(char)
        
        for i in range(1, len(words)):
            self.findEdges(words[i - 1], words[i], in_degree, out_degree)
            
        for node in nodes:
            if node not in in_degree:
                zero_in_degree_queue.append(node)
                
        while zero_in_degree_queue:
            predecessor = zero_in_degree_queue.popleft()
            result += predecessor
            
            if predecessor in out_degree:
                for node in out_degree[predecessor]:
                    in_degree[node].discard(predecessor)
                    if not in_degree[node]:
                        zero_in_degree_queue.append(node)
                del out_degree[predecessor]
        
        if out_degree:
            return ""
        return result
                
        
    def findEdges(self, word1, word2, in_degree, out_degree):
        length = min(len(word1), len(word2))
        for i in range(length):
            if word1[i] != word2[i]:
                if word1[i] not in out_degree:
                    out_degree[word1[i]] = sets.Set()
                if word2[i] not in in_degree:
                    in_degree[word2[i]] = sets.Set()
                out_degree[word1[i]].add(word2[i])
                in_degree[word2[i]].add(word1[i])
                break

#DFS
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        # Find ancestors of each node by DFS.
        nodes, ancestors = sets.Set(), {}
        for i in xrange(len(words)):
            for c in words[i]:
                nodes.add(c)
        for node in nodes:
            ancestors[node] = []
        for i in xrange(1, len(words)):
            self.findEdges(words[i - 1], words[i], ancestors)

        # Output topological order by DFS.
        result = []
        visited = {}
        for node in nodes:
            if self.topSortDFS(node, node, ancestors, visited, result):
                return ""
        
        return "".join(result)


    # Construct the graph.
    def findEdges(self, word1, word2, ancestors):
        min_len = min(len(word1), len(word2))
        for i in xrange(min_len):
            if word1[i] != word2[i]:
                ancestors[word2[i]].append(word1[i])
                break


    # Topological sort, return whether there is a cycle.
    def topSortDFS(self, root, node, ancestors, visited, result):
        if node not in visited:
            visited[node] = root
            for ancestor in ancestors[node]:
                if self.topSortDFS(root, ancestor, ancestors, visited, result):
                    return True
            result.append(node)
        elif visited[node] == root:
            # Visited from the same root in the DFS path.
            # So it is cyclic.
            return True
        return False
