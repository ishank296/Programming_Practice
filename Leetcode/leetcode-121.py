# Best time to buy and sell stock
# to maximize profit
# Maximum profit that can achieved from the transaction

class Solution:

    def maxprofit(self,prices: list[int])->int:
        max_profit = 0
        buy = prices[0]
        for price in prices:
            if price < buy: buy = price
            if price > buy: max_profit = max(max_profit,price - buy)
        return max_profit


if __name__ == "__main__":
    s = Solution()
    price_list = [7,1,5,3,6,4]
    print(s.maxprofit(price_list))