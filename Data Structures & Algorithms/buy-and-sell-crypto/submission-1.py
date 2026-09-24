class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       left = 0
       right = 0
       profit = 0

       while right + 1< len(prices):
         currentProfit = prices[right+1] -prices[left]
         if currentProfit >= 0:
            right+=1
            if currentProfit > profit:
                profit = currentProfit
         else:
            right+=1
            left = right
       return profit
        
         
         



