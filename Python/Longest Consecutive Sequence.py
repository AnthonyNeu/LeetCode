"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
"""

# O(n) time
# O(n) space
class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        if len(num) is 0:
            return 0
        result, lengths = 1, {key: 0 for key in num}
        
        for number in num:
            if not lengths.has_key(number):
                continue
            lower,upper = number,number
            while lengths.has_key(upper+1):
                upper +=1
                del lengths[upper]
            while lengths.has_key(lower-1):
                lower -=1
                del lengths[lower]
            if lower != upper:
                del lengths[number]
            result = max(result,upper - lower + 1)
        
        return result


# O(n) time
# O(n) space
class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        result, lengths = 1, {key: 0 for key in num}
        for i in num:
            if lengths[i] == 0:
                lengths[i] = 1
                left, right = lengths.get(i - 1, 0), lengths.get(i + 1, 0)
                length = 1 + left + right
                result, lengths[i - left], lengths[i + right] = max(result, length), length, length
        return result