/*
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
*/


/**
 * Definition for an interval.
 * public class Interval {
 *     int start;
 *     int end;
 *     Interval() { start = 0; end = 0; }
 *     Interval(int s, int e) { start = s; end = e; }
 * }
 */
public class Solution {
    public List<Interval> merge(List<Interval> intervals) {
        List<Interval> result = new ArrayList<>();
        for (Interval interval : intervals) {
            insert(result, interval);
        }
        return result;
    }
    
    private void insert(List<Interval> intervals, Interval newInterval) {
        int idx = 0;
        while(intervals.size() > idx) {
            Interval interval = intervals.get(idx);
            if (interval.start > newInterval.end) {
                intervals.add(idx, newInterval);
                return;
            } else if (interval.end < newInterval.start) {
                idx ++;
                continue;
            } else {
                newInterval.start = Math.min(interval.start, newInterval.start);
                newInterval.end = Math.max(interval.end, newInterval.end);
                intervals.remove(idx);
            }
        }
        intervals.add(newInterval);
    }
}
