class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        profit = 0
        
        while sell < len(prices):
            if prices[buy] < prices[sell]:          # If the price is lower than the buy price
                diff = prices[sell] - prices[buy]   
                profit = max(profit, diff)          # Update the max profit
            else:
                buy = sell                          # Set the buy price to the sell price
            sell += 1
                
        return profit