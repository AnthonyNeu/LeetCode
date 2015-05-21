/*
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
*/

public class Solution {
    public int longestConsecutive(int[] nums) {
        HashMap<Integer, Integer> hs = new HashMap<Integer, Integer>();
        for(int i: nums){
            hs.put(i, 0);
        }
        int maxl = 1;
        for(int i: nums){
            if (hs.get(i) == 1) continue;

            int tmp = i;
            int current_max = 1;
            while(hs.containsKey(tmp+1)){
                current_max ++;
                tmp ++;
                hs.put(tmp, 1);
            }

            tmp = i;
            while(hs.containsKey(tmp-1)){
                current_max ++;
                tmp --;
                hs.put(tmp, 1);
            }

            maxl = Math.max(current_max, maxl);
        }

        return maxl;
    }
}