"""
Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
"""

# Time:O(nlogn)
# Space:O(n)
class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        num = [str(x) for x in num]
        num.sort(cmp=lambda x, y: cmp(y + x, x + y))
        largest = ''.join(num)
        return largest.lstrip('0') or '0'


# Time:O(nlogn)
# Space:O(n)
class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        dic = {0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}

        for number in num:
            e = 0
            while number/10**e >=10:
                e +=1

            dic[number/10**e].append(number)

        largest = []
        for i in reversed(xrange(10)):
            num = [str(x) for x in dic[i]]
            num.sort(cmp=lambda x, y: cmp(y + x, x + y))
            largest = largest + num
        result = ''.join(largest)
        return result.lstrip('0') or '0'