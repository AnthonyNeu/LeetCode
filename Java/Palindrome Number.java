/*
Question:
Determine whether an integer is a palindrome. Do this without extra space.
Example Questions Candidate Might Ask:
Q: Does negative integer such as –1 qualify as a palindrome?
A: For the purpose of discussion here, we define negative integers as non-palindrome.
*/


public class Solution {
    public boolean isPalindrome(int x) {
        if(x < 0)
            return false;
        //find the number of digits of x
        int digit = 0;
        while(x/(Math.pow(10,digit))>10)
        {
            digit++;
        }
        while(x!=0)
        {
            int left = (int)(x/(Math.pow(10,digit)));
            int right = x%10;
            if(left!=right)
                return false;
            //delete the leading number and tailing number
            x = x - left * (int)(Math.pow(10,digit));
            x = x/10;
            digit = digit -2;
        }
        return true;
    }
}