"""
Description:

Count the number of prime numbers less than a non-negative number, n

click to show more hints.

References:
How Many Primes Are There?
https://primes.utm.edu/howmany.html

Sieve of Eratosthenes
http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
"""

class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        if n == 0 or n == 1:
            return 0
        A = [True for _ in xrange(n)]
        A[0] = A[1] = False
        i = 2
        while i * i < n:
            if A[i] is True:
                j = i
                while i*j < n:
                    A[i * j] = False
                    j+=1
            i+=1
        
        return sum(A)
