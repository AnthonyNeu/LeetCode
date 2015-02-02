"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
"""

class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        result = []
        num = sorted(num)
        for i in range(len(num)):
            if i > 0 and num[i] == num[i-1]:
                continue
            x = 0 - num[i]
            left = i+1
            right = len(num)-1
            while left < right:
                if left > i + 1 and num[left] == num[left-1]:
                    left +=1
                    continue
                if right < len(num) -1 and num[right] == num[right+1]:
                    right -=1
                    continue
                if num[left] + num[right] == x:
                    tmp = []
                    tmp.append(num[i])
                    tmp.append(num[left])
                    tmp.append(num[right])
                    result.append(tmp)
                    left +=1
                    right-=1
                elif num[left] + num[right] < x:
                    left += 1
                else:
                    right -=1
        return result