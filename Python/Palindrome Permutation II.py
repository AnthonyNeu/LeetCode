"""
Given a string s, return all the palindromic permutations (without duplicates) of it. Return an empty list if no palindromic permutation could be form.

For example:

Given s = "aabb", return ["abba", "baab"].

Given s = "abc", return [].

Hint:

If a palindromic permutation exists, we just need to generate the first half of the string.
To generate all distinct permutations of a (half of) string, use a similar approach from: Permutations II or Next Permutation.
"""

class Solution1(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) == 1: return [s]
        elif len(s) == 0 or not self.canPermutePalindrome(s): return []
        
        table = {}
        for char in s:
            if char not in table:
                table[char] = 1
            else:
                table[char] += 1
        
        seq, unique = '', ''
        for key, value in table.iteritems():
            if value % 2 == 0:
                seq += ''.join([key] * (value / 2))
            elif value == 1:
                unique = key
            else:
                seq += key
                unique = key

        permutations = self.permuteUnique(sorted(seq))
        
        result = []
        for permutation in permutations:
            result.append(permutation + unique + permutation[::-1])
        return result
        
    def permuteUnique(self, strings):
        result = []
        used = [False] * len(strings)
        self.permuteRecu(result, strings, [], used)
        return result
        
    def permuteRecu(self, result, strings, cur, used):
        if len(cur) == len(strings):
            result.append(''.join(cur))
        
        prev_idx = -1
        for i in range(len(strings)):
            if used[i] or (prev_idx != -1 and strings[prev_idx] == strings[i]):
                continue
            used[i] = True
            cur.append(strings[i])
            self.permuteRecu(result, strings, cur, used)
            cur.pop()
            used[i] = False
            prev_idx = i
    
    def canPermutePalindrome(self, s):
        return sum(v % 2 for v in collections.Counter(s).values()) < 2


class Solution2(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        d = collections.Counter(s)
        m = tuple(k for k, v in d.iteritems() if v % 2)
        p = ''.join(k*(v/2) for k, v in d.iteritems())
        return [''.join(i + m + i[::-1]) for i in set(itertools.permutations(p))] if len(m) < 2 else []
