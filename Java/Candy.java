/*
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?
*/

//O(n) time, O(n) space
public class Solution {
    public int candy(int[] ratings) {
        int[] result = new int[ratings.length];
        for(int i = 0 ; i< result.length ; i ++)
            result[i] = 1;
        
        
        for(int i = 1 ; i < ratings.length ; i ++){
            if(ratings[i] > ratings[i-1])
                result[i] = result[i-1] + 1;
        }
        
        for(int i = ratings.length - 1 ; i >= 1 ; i --){
            if(ratings[i] < ratings[i-1] && result[i-1] <= result[i])
                result[i-1] = result[i] + 1;
        }
        
        int sum = 0;
        for(int i = 0 ; i< result.length ; i ++)
            sum += result[i];
        return sum;
    }
}