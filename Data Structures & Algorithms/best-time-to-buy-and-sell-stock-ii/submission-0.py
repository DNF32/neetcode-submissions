class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        potencialBuy = 0 
        totalProfit = 0 

        for i in range(len(prices)):
            sellPrice = prices[i]
            buyPrice = prices[potencialBuy]

            if buyPrice < sellPrice:
                totalProfit += sellPrice - buyPrice
            potencialBuy = i
        return totalProfit

        