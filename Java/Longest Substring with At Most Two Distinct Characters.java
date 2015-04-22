/*
Given a string S, find the length of the longest substring T that contains at most two distinct characters.
For example,
Given S = “eceba”,
T is "ece" which its length is 3.
*/

//O(n^2)
public int lengthOfLongestSubstringTwoDistinct(String s) {
   int start = 0, end = -1, maxLen = 0;
   for (int k = 1; k < s.length(); k++) 
   {
      if (s.charAt(k) == s.charAt(k - 1)) continue;
      if (end >= 0 && s.charAt(end) != s.charAt(k)) 
      {
      	maxLen = Math.max(k - start, maxLen);
		start = end + 1; 
	}
		end = k - 1; 
	}
   return Math.max(s.length() - start, maxLen);
}

//O(n^2), with hash table
public int lengthOfLongestSubstringTwoDistinct(String s) {
   int[] count = new int[256];
   int i = 0, numDistinct = 0, maxLen = 0;
   for (int j = 0; j < s.length(); j++) {
      if (count[s.charAt(j)] == 0) numDistinct++;
      count[s.charAt(j)]++;
      while (numDistinct > 2) {
         count[s.charAt(i)]--;
         if (count[s.charAt(i)] == 0) numDistinct--;
         i++;
     }
      maxLen = Math.max(j - i + 1, maxLen);
   }
   return maxLen;
}