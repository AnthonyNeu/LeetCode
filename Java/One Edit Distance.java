/*
Given two strings S and T, determine if they are both one edit distance apart. Hint:
1. If | n – m | is greater than 1, we know immediately both are not one-edit distance apart.
2. It might help if you consider these cases separately, m == n and m ≠ n.
3. Assume that m is always ≤ n, which greatly simplifies the conditional statements.
If m > n, we could just simply swap S and T.
4. If m == n, it becomes finding if there is exactly one modified operation. 
If m != n, you do not have to consider the delete operation. Just consider the insert operation in T.
*/

public boolean isOneEditDistance(String s, String t) {
        int m = s.length(), n = t.length();
        if (m > n) return isOneEditDistance(t, s);
        if (n - m > 1) return false;
        int i = 0, shift = n - m;
        while (i < m && s.charAt(i) == t.charAt(i)) i++;
        //s == t, which returns false
        //or n = m+1 and last character of t is redundant
        if (i == m) return shift>0;
        if (shift == 0) i++;
        while (i < m && s.charAt(i) == t.charAt(i + shift)) i++;
        return i == m;
    }