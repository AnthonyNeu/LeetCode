"""
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""

class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        if len(digits) == 0:
            return [""]
        table = {'0':'0','1':'1','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        result = []
        for i in range(len(digits)):
            if i == 0:
                tmp = table[digits[i]]
                for j in range(len(tmp)):
                    result.append(tmp[j])
            else:
                previous = result
                result = []
                tmp = table[digits[i]]
                for k in range(len(tmp)):
                    for j in range(len(previous)):
                        result.append(previous[j] + tmp[k])
        return result

class Solution:
    def letterCombinations(self, digits):
        lookup, res = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"], []
        self.letterCombinationsRecur(lookup, res, "", digits)
        return res
        
    def letterCombinationsRecur(self, lookup, res, current, digits):
        if digits == "":
            res.append(current)
            return
        for choice in lookup[int(digits[0])]:
            self.letterCombinationsRecur(lookup, res, current + choice, digits[1:])