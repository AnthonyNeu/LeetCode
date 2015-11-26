"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

prices = [1, 2, 3, 0, 2]
maxProfit = 3
transactions = [buy, sell, cooldown, buy, sell]
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) == 1:
            return 0
        must_sell = [0 for _ in range(len(prices))]
        must_buy = [0 for _ in range(len(prices))]
        must_buy[0] = -prices[0]
        must_buy[1] = -prices[1]
        for i in range(1, len(prices)):
            gain_or_lose = prices[i] - prices[i - 1]
            must_sell[i] = max(must_sell[i - 1] + gain_or_lose, must_buy[i - 1] + prices[i])
            if i >= 2:
                must_buy[i] = max(must_buy[i - 1] - gain_or_lose, must_sell[i - 2] - prices[i])
        return max(must_sell)

# from https://leetcode.com/discuss/71354/share-my-thinking-process
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        sell, buy, prev_sell, prev_buy = 0, -prices[0], 0, 0
        for price in prices:
            prev_buy = buy
            buy = max(prev_sell - price, prev_buy)
            prev_sell = sell
            sell = max(prev_buy + price, prev_sell)
        return sell
