/*
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.
*/

//O(n) time,O(1) space
public class Solution {
    public int removeDuplicates(int[] nums) {
        if(nums.length == 0) return 0;
        
        int idx = 0,count = 1;
        for(int i=1;i<nums.length;i++){
            if((nums[i-1] == nums[i] && count == 1) || nums[i-1] != nums[i]){
                if(nums[i-1] == nums[i])
                    count++;
                else
                    count = 1;
                nums[++idx] = nums[i];
            }
        }
        return idx+1;
    }
}

public class Solution {
    public int removeDuplicates(int[] nums) {
        int index = 0;
        for(int i=0;i<nums.length;i++){
            if(i > 0 && i < nums.length-1 && nums[i-1] == nums[i] && nums[i+1] == nums[i])
                continue;
            nums[index++] = nums[i];
        }
        return index;
    }
}

public class Solution {
    public int removeDuplicates(int[] nums) {
        int n  = nums.length;
        if(n<=2) return n;
        int index = 2;
        for(int i=2;i<n;i++){
            if(nums[index-2] != nums[i])
                nums[index++] = nums[i];
        }
        return index;
    }
}