"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

  [
    ["aa","b"],
    ["a","a","b"]
  ]
"""

# Time:  O(n^2 ~ 2^n)
# Space: O(n^2)
# dynamic programming solution
class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        N = len(s)
        table = [[False for _ in xrange(N)] for _ in xrange(N)]
        
        for i in xrange(N):
            table[i][i] = True
            
        for i in xrange(N-1):
            if s[i] == s[i+1]:
                table[i][i+1] = True
                
        for length in xrange(3,N+1):
            for i in xrange(N-length+1):
                j = i + length - 1
                if s[i] == s[j] and table[i+1][j-1]:
                    table[i][j] = True
        result = []                    
        self.partitionHelper(table,0,[],result,s)
        
        return result
                    
    
    def partitionHelper(self,table,start,current,result,s):
        for j in xrange(start,len(s)):
            if table[start][j] == True:
                current.append(s[start:j+1])
                
                if j == len(s)-1:
                    cur = list(current)
                    result.append(cur)
                else:
                    self.partitionHelper(table,j+1,current,result,s)
                    
                current.pop()

class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        n = len(s)
        
        is_palindrome = [[0 for j in xrange(n)] for i in xrange(n)]
        for i in reversed(xrange(0, n)):
            for j in xrange(i, n):
                is_palindrome[i][j] = s[i] == s[j] and ((j - i < 2 ) or is_palindrome[i + 1][j - 1])
        
        sub_partition = [[] for i in xrange(n)]
        for i in reversed(xrange(n)):
            for j in xrange(i, n):
                if is_palindrome[i][j]:
                    if j + 1 < n:
                        for p in sub_partition[j + 1]:
                            sub_partition[i].append([s[i:j + 1]] + p)
                    else:
                        sub_partition[i].append([s[i:j + 1]])
                        
        return sub_partition[0]

# Time:  O(2^n)
# Space: O(n)
# recursive solution
class Solution2:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        result = []
        self.partitionRecu(result, [], s, 0)
        return result
        
    def partitionRecu(self, result, cur, s, i):
        if i == len(s):
            result.append(list(cur))
        else:
            for j in xrange(i, len(s)):
                if self.isPalindrome(s[i: j + 1]):
                    cur.append(s[i: j + 1])
                    self.partitionRecu(result, cur, s, j + 1)
                    cur.pop()
                
    def isPalindrome(self, s):
        for i in xrange(len(s) / 2):
            if s[i] != s[-(i + 1)]:
                return False
        return True