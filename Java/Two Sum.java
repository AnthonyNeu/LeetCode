/*
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
*/

// Hash table: O(n) runtime, O(n) space
public class Solution {
    public int[] twoSum(int[] numbers, int target) {
        HashMap <Integer,Integer>table = new HashMap<Integer,Integer>();
        for(int i = 0;i<numbers.length;i++)
        {
            if(!table.containsKey(numbers[i]))
            {
                table.put(target - numbers[i],i);
            }
            else
            {
                int idx = table.get(numbers[i]);
                return new int[]{Math.min(idx,i)+1,Math.max(idx,i)+1};
            }
        }
        throw new IllegalArgumentException("no 2sum solution");
    }
}