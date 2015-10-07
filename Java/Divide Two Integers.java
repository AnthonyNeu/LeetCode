/*
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
*/

/* O(log n) times, O(1) space */
/*
a = (2^n * an + ... + 2^1 * a1 + 2^0 * a0)
We calculate the result of 2^n * an divide by divisor and sum up all the result.
Similarly, we transfer the number into a new number based on divisor:
a = (d^n * an + ... + d^1 * a1 + d^0 * a0)
And then sum up all the an*d^n to get the result.
*/
public class Solution {
    public int divide(int dividend, int divisor) {
        int result = 0;
        
        /* this method cannot give right answer for this situation */
        if (dividend == Integer.MIN_VALUE && divisor == -1) {
            return Integer.MAX_VALUE;
        }
        
        long dvd = Math.abs((long) dividend), dvs = Math.abs((long) divisor);
        boolean sign = (dividend > 0 && divisor < 0) || (dividend < 0 && divisor > 0);
        
        while (dvd >= dvs) {
            int count = 1;
            long dd = dvs;
            
            while (dvd >= dd) {
                dvd -= dd;
                result += count;
                
                if (dd < (Integer.MAX_VALUE >> 1)) {
                    dd += dd;
                    count += count;
                }
            }
        }
        
        if (sign) return -1 * result;
        return result;
    }
}
