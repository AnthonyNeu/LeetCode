"""
Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"], 
Return:

[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
Note: For the return value, each inner list's elements must follow the lexicographic order.
"""

# Time:  O(n^2)
# Space: O(n)
class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        result = []
        visited = [False] * len(strings)
        strings = sorted(strings)
        for i in range(len(strings)):
            if visited[i]: continue
            result.append([strings[i]])
            for j in range(len(strings)):
                if i == j or len(strings[i]) != len(strings[j]) or visited[j]: continue
                is_same = True
                distance = (ord(strings[j][0]) - ord(strings[i][0]) + 26) % 26
                for m in range(1, len(strings[i])):
                    if (ord(strings[j][m]) - ord(strings[i][m]) + 26) % 26 != distance:
                        is_same = False
                        break
                if is_same:
                    result[-1].append(strings[j])
                    visited[j] = True
        return result

# Time:  O(nlogn)
# Space: O(n)
class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        groups = collections.defaultdict(list)
        for s in strings:  # Grouping.
            groups[self.hashStr(s)].append(s)

        result = []
        for key, val in groups.iteritems():
            result.append(sorted(val))
        
        return result

    def hashStr(self, s):
        base = ord(s[0])
        hashcode = ""
        for i in xrange(len(s)):
            if ord(s[i]) - base >= 0:
                hashcode += unichr(ord('a') + ord(s[i]) - base)
            else:
                hashcode += unichr(ord('a') + ord(s[i]) - base + 26)
        return hashcode
