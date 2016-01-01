"""
You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.

Note:
You may assume that you have an infinite number of each kind of coin.
"""

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        visited, cur, result, next_level = [False] * (amount + 1), [0], 0, []
        while cur:
            result += 1
            for coin in coins:
                for v in cur:
                    new_v = v + coin
                    if new_v == amount:
                        return result
                    elif new_v > amount:
                        continue
                    elif not visited[new_v]:
                        visited[new_v] = True
                        next_level.append(new_v)
            cur, next_level = next_level, []
        return -1
