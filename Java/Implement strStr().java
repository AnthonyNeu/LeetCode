/*
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
*/

//Karp-Rabin Algorithm
public class Solution {
    public int strStr(String haystack, String needle) {
        int M = haystack.length();
        int N = needle.length();
        if (M < N)
        {
            return -1;
        }
        if(M==N && haystack.equals(needle))
        {
            return 0;
        }
        int pattern = hash(needle);
        for(int i = 0;i< M - N +1;i++)
        {
            String temp = haystack.substring(i,i+N);
            if(hash(temp) == pattern)
            {
                if(temp.equals(needle)){
                    return i;
                }
            }
        }
        return -1;
    }
    
    private int hash(String s)
    {
        int hash = 0;
        for(int i = 0;i<s.length();i++)
        {
            hash += (int)(s.charAt(i)) * Math.pow(10,i);
        }
        return hash;
    }
}

//O(nm) runtime, O(1) space – Brute force:
public int strStr(String haystack, String needle) {
   for (int i = 0; ; i++) {
   	for (int j = 0; ; j++) {
   		if (j == needle.length()) return i;
   		if (i + j == haystack.length()) return -1;
   		if (needle.charAt(j) != haystack.charAt(i + j)) break;
   	} 
   }
}