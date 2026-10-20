class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_price = float('inf')
        difference = 0 
        best = 0

        for i in range(0, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            best = prices[i] - min_price
            if best > difference:
                difference = best   
       
        return difference 
        
        








            
            