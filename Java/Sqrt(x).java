/*
Implement int sqrt(int x).

Compute and return the square root of x.
*/

public class Solution {
    public int mySqrt(int x) {
        int lo = 1;
        int hi = x / 2;
        
        if(x < 2) return x;

        while (hi >= lo) {     
            int mid = lo+(hi-lo)/2;
            if (x / mid < mid) {
                hi = mid-1;
            } else {
                lo = mid+1;  
            }
        }
        return hi;
    }
}
