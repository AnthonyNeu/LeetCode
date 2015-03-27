"""
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

Return 0 if the array contains less than 2 elements.

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.

"""

class Solution:
    # @param num, a list of integer
    # @return an integer
    def maximumGap(self, num):
        if len(num) < 2:
            return 0
        Max = -1
        Min = 9223372036854775807
        for i in xrange(len(num)):
            if num[i] < Min:
                Min = num[i]
            if num[i] > Max:
                Max = num[i]

        gap = (Max - Min)/len(num) + 1
        minGap = [-1 for _ in range((Max - Min)/gap + 1)]
        maxGap = [-1 for _ in range((Max - Min)/gap + 1)]

        for i in xrange(len(num)):
            if minGap[(num[i]-Min)/gap] == -1:
                minGap[(num[i]-Min)/gap] = num[i]
                maxGap[(num[i]-Min)/gap] = num[i]
            else:
                if minGap[(num[i]-Min)/gap] > num[i]:
                    minGap[(num[i]-Min)/gap] = num[i]
                elif maxGap[(num[i]-Min)/gap] < num[i]:
                    maxGap[(num[i]-Min)/gap] = num[i]

        maxInterval = 0
        start = minGap[0]
        for i in xrange(len(minGap)):
            if minGap[i] != maxGap[i] or (minGap[i] == maxGap[i] and maxGap[i] != -1):
                end = minGap[i]
                maxInterval = max(maxInterval,end - start)
                start = maxGap[i]
        return max(maxInterval,end - start) 