"""
Best Time to Buy and Sell Stock

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
"""

"""
Solution： Get the minimum price of the stock by iterating all the price. Running time:O(n),space:O(1). 
"""


class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
    	if len(prices) == 0:
    		return 0
        max_profit = 0
        min_price = 9223372036854775807
        for price in prices:
            min_price = min(price,min_price)
            max_profit = max(max_profit,price - min_price)
        return max_profit