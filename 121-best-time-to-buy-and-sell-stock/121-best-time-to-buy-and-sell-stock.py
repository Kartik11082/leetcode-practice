class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell, maxProfit = 0, 0, 0

        while sell < len(prices):
            if prices[buy] > prices[sell]:
                buy = sell
                sell += 1
            else:
                maxProfit = max(prices[sell] - prices[buy], maxProfit)
                sell += 1

        return maxProfit