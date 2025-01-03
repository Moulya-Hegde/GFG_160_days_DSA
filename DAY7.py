'''
Stock Buy and Sell – Multiple Transaction Allowed
Difficulty: Medium
The cost of stock on each day is given in an array price[]. Each day you may decide to either buy or sell the stock i at price[i], you can even buy and sell the stock on the same day. Find the maximum profit that you can get.

Note: A stock can only be sold if it has been bought previously and multiple stocks cannot be held on any given day.
'''
from typing import List


class Solution:
    def maximumProfit(self, prices) -> int:
        low=high=prices[0]
        profit=0
        for i in range(1,len(prices)):
            if prices[i]<prices[i-1] :
                profit+=high-low
                low=high=prices[i]
            elif prices[i]>high:
                high=prices[i]
        if high!=low:
            profit+=high-low
        return profit   