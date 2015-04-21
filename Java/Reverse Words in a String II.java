/*
Similar to Question [6. Reverse Words in a String], but with the following constraints:
“The input string does not contain leading or trailing spaces and the words are always separated by a single space.”
Could you do it in-place without allocating extra space?
*/

//O(n) runtime, O(1) space – In-place reverse:
public void reverseWords(char[] s) {
   reverse(s, 0, s.length);
   for (int i = 0, j = 0; j <= s.length; j++) 
   {
      if (j == s.length || s[j] == ' ') {
         reverse(s, i, j);
         i = j + 1;
	} 
}
}

private void reverse(char[] s, int begin, int end) {
   for (int i = 0; i < (end - begin) / 2; i++) {
      char temp = s[begin + i];
      s[begin + i] = s[end - i - 1];
      s[end - i - 1] = temp;
} 
}