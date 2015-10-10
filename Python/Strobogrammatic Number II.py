"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

For example,
Given n = 2, return ["11","69","88","96"].

Hint:

Try to use recursion and notice that it should recurse with n - 2 instead of n - 1.

"""

class Solution(object):
    lookup = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return self.findStrobogrammaticRecu(n, n)
    
    def findStrobogrammaticRecu(self, n, k):
        if k == 0:
            return [""]
        if k == 1:
            return ["1", "8", "0"]
            
        result = []
        
        for num in self.findStrobogrammaticRecu(n, k - 2):
            for key, value in self.lookup.iteritems():
                if n != k or key != '0':
                    result.append(key + num + value)
        return result
