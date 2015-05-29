/*
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
*/

public class Solution {
    public void nextPermutation(int[] nums) {
        if(nums.length == 0) return;
        int partitionNum = nums.length-1;
        while(partitionNum>0){
            if(nums[partitionNum-1] < nums[partitionNum])
                break;
            partitionNum--;
        }
        if(partitionNum > 0){
            int changeNum = nums.length-1;
            while(changeNum >= 0 && nums[changeNum]<= nums[partitionNum-1])
                changeNum--;
            int swap = nums[changeNum];
            nums[changeNum] = nums[partitionNum-1];
            nums[partitionNum-1] = swap;
        }
        int end = nums.length-1;
        while(end>partitionNum){
            int swap = nums[end];
            nums[end] = nums[partitionNum];
            nums[partitionNum] = swap;
            end--;
            partitionNum++;
        }
    }
}