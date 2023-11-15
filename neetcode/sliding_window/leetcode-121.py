# Best Time to Buy and Sell Stock
#
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single
# day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        cur_profit = 0
        start,end = 0,1
        while start < len(prices) and end < len(prices):
            if prices[start] < prices[end]:
                cur_profit = prices[end] - prices[start]
                max_profit = max(cur_profit,max_profit)
            else:
                start=end
            end+=1
        return max_profit

    def display(self,prices):
        print(f"Result for input {prices}: ",self.maxProfit(prices))


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    s = Solution()
    s.display(prices)
    prices = [7, 6, 4, 3, 1]
    s.display(prices)
