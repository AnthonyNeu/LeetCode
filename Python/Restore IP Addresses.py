"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.
For example:
Given "25525511135",
return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
"""

class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        M = len(s)
        result = []
        for i in range(1,min(4,M-2)):
            for j in range(i+1,min(i+4,M-1)):
                for k in range(j+1,min(j+4,M)):
                    s1 = s[:i]
                    s2 = s[i:j]
                    s3 = s[j:k]
                    s4 = s[k:]
                    if self.isValid(s1) and self.isValid(s2) and self.isValid(s3) and self.isValid(s4):
                        result.append(s1 + '.' + s2 + '.' + s3 +'.' +s4)
        return result
        
    def isValid(self,s):
        if len(s) > 3 or len(s) == 0 or (s[0] == '0' and len(s) > 1) or int(s) > 255:
            return False
        return True

class Solution:
    def restoreIpAddresses(self, s):
        result = []
        self.restoreIpAddressesRecur(result, s, "", 0)
        return result
        
    def restoreIpAddressesRecur(self, result, s, current, dots):
        # pruning to improve performance
        if (4 - dots) * 3 < len(s):
            return
        if dots == 3:
            if self.isValid(s):
                result.append(current + s)
        else:
            for i in range(3):
                if len(s) > i and self.isValid(s[:i + 1]):
                    self.restoreIpAddressesRecur(result, s[i + 1:], current + s[:i + 1] + '.', dots + 1)
        
    def isValid(self, s):
        if len(s) == 0 or (s[0] == "0" and s != "0"):
            return False
        return int(s) < 256