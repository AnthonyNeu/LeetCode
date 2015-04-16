"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
"""

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        if len(intervals) == 0:
            return [newInterval]
        if newInterval is []:
            return intervals
        if newInterval.end < intervals[0].start:
            intervals.insert(0,newInterval)
            return intervals
        if newInterval.start > intervals[len(intervals)-1].end:
            intervals.append(newInterval)
            return intervals
        if newInterval.end == intervals[0].start:
            tempInterval = Interval(newInterval.start,intervals[0].end)
            intervals.pop(0)
            intervals.insert(0,tempInterval)
            return intervals
        if newInterval.start == intervals[len(intervals)-1].end:
            tempInterval = Interval(intervals[len(intervals)-1].start,newInterval.end)
            intervals.pop()
            intervals.append(tempInterval)
            return intervals
        
        first,last = 0,0
        while first < len(intervals) and newInterval.start > intervals[first].end:
            first +=1
        while last < len(intervals) and newInterval.end >= intervals[last].start:
            last +=1
        
        newStart =  min(intervals[first].start,newInterval.start)
        newEnd =  max(intervals[last-1].end,newInterval.end)
        
        return intervals[:first] + [Interval(newStart,newEnd)] + intervals[last:]

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        return self.merge(intervals + [newInterval])
        
    def merge(self, intervals):
        if not intervals:
            return intervals
        intervals.sort(key = lambda x: x.start)
        result = [intervals[0]]
        for i in xrange(1, len(intervals)):
            prev, current = result[-1], intervals[i]
            if current.start <= prev.end: 
                prev.end = max(prev.end, current.end)
            else:
                result.append(current)
        return result	