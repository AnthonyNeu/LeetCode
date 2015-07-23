/*
Given an array of integers, every element appears three times except for one. Find that single one.
Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
*/


public class Solution {
    public int singleNumber(int[] nums) {
        final int W = Integer.SIZE;
        int[] count = new int[W];
        
        for(int i = 0 ; i < nums.length ; i++){
            for(int j = 0 ; j < W ; j ++){
                count[j] += (nums[i] >> j) & 1;
                count[j] %= 3;
            }
        }
        
        int result = 0;
        for(int i = 0 ; i < W ; i ++){
            result += (count[i] << i);
        }
        return result;
    }
}


public class Solution {
    public int singleNumber(int[] nums) {
        int one = 0, two = 0, three = 0;
        for(int i = 0;i < nums.length;i++){
            two |= one & nums[i];
            one ^= nums[i];
            three = one&two;
            two &= ~three;
            one &= ~three;
        }
        return one;
    }
}