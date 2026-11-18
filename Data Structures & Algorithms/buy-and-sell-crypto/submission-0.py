class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = 0
        sell = 0

        for index, val in enumerate(prices):
            if val > prices[sell]:
                sell = index
            elif val < prices[buy]:
                buy = index
                sell = index
            profit = max(profit,prices[sell] - prices[buy])
            



        if profit < 0:
            return 0
        else:
            return profit