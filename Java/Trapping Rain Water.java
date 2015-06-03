/*
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
*/

//O(n) time,O(n) space
public class Solution {
    public int trap(int[] height) {
        int[] max_left = new int[height.length];
        int[] max_right = new int[height.length];
        
        for(int i = 1;i<height.length;i++){
            max_left[i] = Math.max(max_left[i-1],height[i-1]);
            max_right[height.length-1-i] = Math.max(max_right[height.length-i],height[height.length-i]);
        }
        
        int sum = 0;
        for(int i=0;i < height.length;i++){
            int h = Math.min(max_left[i],max_right[i]);
            if(h > height[i])
                sum += h - height[i];
        }
        return sum;
    }
}

//O(n) time and O(1) space
public class Solution {
    public int trap(int[] height) {
        int n = height.length;
        int max = 0;
        for(int i=0;i<n;i++)
            if(height[i] > height[max]) max = i;
        int water = 0;
        for(int i = 0,peak = 0;i<max;i++){
            if(height[i] > peak) peak = height[i];
            else water += peak - height[i];
        }
        for(int i = n-1,top = 0;i>=max;i--){
            if(height[i] > top) top = height[i];
            else water += top - height[i];
        }
        return water;
    }
}


//Use stack,O(n) time,O(n) space
public class Solution {
    public int trap(int[] height) {
        Stack<ArrayList<Integer>> stack = new Stack<>();
        int water = 0;
        
        for(int i = 0;i<height.length;i++){
            int h = 0;
            
            while(!stack.empty()){
                //pop all the element in the stack which is smaller or equal than height[i] 
                int bar = stack.peek().get(0);
                int pos = stack.peek().get(1);
                //compute the water by bar, height[i] and the height of water is h
                water += (Math.min(bar,height[i])-h) * (i - pos - 1);
                h = bar;
                if(height[i] < bar)
                    break;
                else
                    stack.pop();
            }
            ArrayList<Integer> temp = new ArrayList<>();
            temp.add(height[i]);temp.add(i);
            stack.push(temp);
        }
        return water;
    }
}