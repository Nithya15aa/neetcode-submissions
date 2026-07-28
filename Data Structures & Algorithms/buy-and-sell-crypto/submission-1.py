class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        b = prices[0] #buy
        for i in range(1,len(prices)):
            profit = max(profit , prices[i]-b)
            b = min (b,prices[i])
        return profit
            
        

        