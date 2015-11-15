"""
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Examples:
"()())()" -> ["()()()", "(())()"]
"(a)())()" -> ["(a)()()", "(a())()"]
")(" -> [""]
"""

class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        from collections import deque
        from sets import Set
        if not s or len(s) == 0:
            return [""]
        result, queue, visited, found = [], deque([s]), Set([s]), False
        while queue:
            cur = queue.popleft()
            if self.is_valid(cur):
                result.append(cur)
                found = True
            if found:
                continue
            # generate all possible next level's strings
            for i in range(len(cur)):
                if cur[i] not in ("(", ")"):
                    continue
                candidate = cur[:i] + cur[i + 1:]
                if candidate not in visited:
                    queue.append(candidate)
                    visited.add(candidate)
        return result
        
    def is_valid(self, s):
        count = 0
        for c in s:
            if c == "(":
                count += 1
            elif c == ")":
                count -= 1
                if count < 0:
                    return False
        return count == 0
