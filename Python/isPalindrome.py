"""
Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.

Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.
"""

#Time O(n)
#Space O(n)
class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
        x_str = str(x)
        for i in xrange(len(x_str)/2):
            if x_str[i] != x_str[-(i+1)]:
                return False

        return True

#Time O(n)
#Space O(1)
class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
        length = 0
        x_copy = x
        while x_copy > 0:
            length +=1
            x_copy/=10

        count = 0
        while count < length/2:
            if (x / (10 ** count)) % 10 != (x/(10 ** (length - count - 1))) % 10:
                return False
            count +=1

        return True


#Time O(n)
#Space O(1)
class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
        copy, reverse = x, 0
        
        while copy:
            reverse *= 10
            reverse += copy % 10
            copy /= 10
        
        return x == reverse