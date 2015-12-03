"""
Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k. For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the sequence of the first 12 super ugly numbers given primes = [2, 7, 13, 19] of size 4.

Note:
(1) 1 is a super ugly number for any given primes.
(2) The given numbers in primes are in ascending order.
(3) 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
"""

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        length, heap, ugly_list, used = len(primes), [], [1], set([1])
        for i in range(length):
            heapq.heappush(heap, (primes[i], 0, primes[i]))
            used.add(primes[i])
        for _ in range(1, n):
            x, i, p = heapq.heappop(heap)
            ugly_list.append(x)
            idx = i + 1
            while (p * ugly_list[idx]) in used:
                idx += 1
            candidate = p * ugly_list[idx]
            heapq.heappush(heap, (candidate, idx, p))
            used.add(candidate)
        return ugly_list[-1]
