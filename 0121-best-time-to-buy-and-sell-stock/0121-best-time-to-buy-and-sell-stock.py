class Solution(object):
    def maxProfit(self, prices):
        min_price = float('inf')  # Start with a large number
        max_profit = 0  
        
        
        for price in prices:
            
            if price < min_price:
                min_price = price
            
            profit = price - min_price
           
            if profit > max_profit:
                max_profit = profit
        
        return max_profit