"""
You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to determine if the starting player can guarantee a win.

For example, given s = "++++", return true. The starting player can guarantee a win by flipping the middle "++" to become "+--+".

Follow up:
Derive your algorithm's runtime complexity.
"""
# backtracking, running time O(n * n!)
class Solution1(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return self.dfs(s)
    
    def dfs(self, s):
        next_moves = self.generatePossibleNextMoves(s)
        
        if len(next_moves) == 0:
            return False
        else:
            for move in next_moves:
                if not self.dfs(move):
                    return True
            return False
        
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s or len(s) == 0:
            return []
        result = []
        for i in range(1, len(s)):
            if s[i] == s[i - 1] == "+":
                result.append(s[:i - 1] + "-" + s[i + 1:])
        return result

# Suppose we have c '++' in the s, so we can store at most 2 ^ c strings in the memo.
# Each one needs to take O(c) time to compute the possible next moves.
class Solution2(object):
    _memo = {}
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        memo = self._memo
        if s not in memo:
            memo[s] = any(s[i:i+2] == '++' and not self.canWin(s[:i] + '-' + s[i+2:])
                          for i in range(len(s)))
        return memo[s]

# Time:  O(n + c^3 * 2^c * logc), n is length of string, c is count of "++"
# Space: O(c * 2^c)
# hash solution.
# We have total O(2^c) game strings,
# and each hash key in hash table would cost O(c),
# each one has O(c) choices to the next one,
# and each one would cost O(clogc) to sort,
# so we get O((c * 2^c) * (c * clogc)) = O(c^3 * 2^c * logc) time.
# To cache the results of all combinations, thus O(c * 2^c) space.
class Solution3(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lookup = {}

        def canWinHelper(consecutives):                                         # O(2^c) time
            consecutives = tuple(sorted(c for c in consecutives if c >= 2))     # O(clogc) time
            if consecutives not in lookup:
                lookup[consecutives] = any(not canWinHelper(consecutives[:i] + (j, c-2-j) + consecutives[i+1:])  # O(c) time
                                           for i, c in enumerate(consecutives)  # O(c) time
                                           for j in xrange(c - 1))              # O(c) time
            return lookup[consecutives]                                         # O(c) time

        # re.findall: O(n) time, canWinHelper: O(c) in depth
        # re.findall find all the consecutive '+..+' in the s
        return canWinHelper(map(len, re.findall(r'\+\++', s)))

# backtracking, running time O(n * n!)
class Solution4(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        chars = list(s) 
        def helper():
            for i in range(len(chars)-1):
                if chars[i] == chars[i+1] == '+':
                    chars[i], chars[i+1] = '-', '-'
                    can_win = helper()
                    chars[i], chars[i+1] = '+', '+'
                    if not can_win:
                        return True
            return False
        return helper()
