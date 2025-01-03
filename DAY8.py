'''
Stock Buy and Sell – Max one Transaction Allowed
Difficulty: Easy
Given an array prices[] of length n, representing the prices of the stocks on different days. The task is to find the maximum profit possible by buying and selling the stocks on different days when at most one transaction is allowed. Here one transaction means 1 buy + 1 Sell. If it is not possible to make a profit then return 0.

Note: Stock must be bought before being sold.
'''
class Solution:
    def maximumProfit(self, prices):
        if not prices or len(prices)<2:
            return 0
        min_p=float("inf")
        max_profit=0
        for i in prices:
            min_p=min(min_p,i)
            profit=i-min_p
            max_profit=max(profit,max_profit)
        return max_profit