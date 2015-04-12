"""
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?
"""

class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        result = [1 for _ in xrange(len(ratings))]
        
        for i in xrange(1,len(ratings)):
            if ratings[i-1] < ratings[i]:
                result[i] = result[i-1] + 1
        
        for i in reversed(xrange(1,len(ratings))):
            if ratings[i-1] > ratings[i] and result[i-1] <= result[i]:
                result[i-1] = result[i] + 1
        return sum(result)