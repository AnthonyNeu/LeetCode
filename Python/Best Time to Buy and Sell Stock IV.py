"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

"""

class Solution:
    # @return an integer as the maximum profit 
    def maxProfit(self, k, prices):
        if k >= len(prices) / 2:
            return self.maxAtMostNPairsProfit(prices)

        return self.maxAtMostKPairsProfit(prices, k)

    def maxAtMostNPairsProfit(self, prices):
        profit = 0
        for i in xrange(len(prices) - 1):
            profit += max(0, prices[i + 1] - prices[i])     
        return profit

    def maxAtMostKPairsProfit(self, prices, k):
        max_buy = [float("-inf") for _ in xrange(k + 1)]
        max_sell = [0 for _ in xrange(k + 1)]

        for i in xrange(len(prices)):
            for j in xrange(1, min(k, i/2+1) + 1):
                max_buy[j] = max(max_buy[j], max_sell[j-1] - prices[i])
                max_sell[j] = max(max_sell[j], max_buy[j] + prices[i])

        return max_sell[k]

class Solution:
    # @return an integer as the maximum profit 
    def maxProfit(self, k, prices):
        if k >= len(prices) / 2:
            return self.maxAtMostNPairsProfit(prices)

        return self.maxAtMostKPairsProfit(prices, k)

    def maxAtMostNPairsProfit(self, prices):
        profit = 0
        for i in xrange(len(prices) - 1):
            profit += max(0, prices[i + 1] - prices[i])     
        return profit

    def maxAtMostKPairsProfit(self, prices, k):
        #t[i][j] = Math.max(t[i][j - 1], prices[j] + tmpMax) gives us the maximum price when we sell at this price; 
        # tmpMax = Math.max(tmpMax, t[i - 1][j - 1] - prices[j]) gives us the value when we buy at this price and leave this value for prices[j+1].
        max_sell = [[0 for _ in xrange(len(prices))] for _ in xrange(k+1)]
        
        for i in xrange(1,k+1):
            tempMax = -prices[0]
            for j in xrange(1,len(prices)):
                max_sell[i][j] = max(max_sell[i][j-1],prices[j] + tempMax)
                tempMax = max(tempMax,max_sell[i-1][j-1] - prices[j])
            
        return max_sell[k][len(prices)-1]