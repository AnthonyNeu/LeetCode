/*
The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.
*/


public class Solution {
    public String getPermutation(int n, int k) {
        StringBuffer sb = new StringBuffer();
        StringBuffer res = new StringBuffer();
        int total = 1;
        for (int i = 1; i <= n; ++i) {
            total = total * i;
            sb.append(i);
        }
        k--;
        while(n != 0) {
            total = total / n;
            int idx = k / total;
            res.append(sb.charAt(idx));
            k = k % total;
            sb.deleteCharAt(idx);
            n--;
        }
        return res.toString();
    }
}