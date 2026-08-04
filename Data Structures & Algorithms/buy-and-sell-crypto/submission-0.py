class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # time complexity = O(n) because we are looping through the integer array n times 
        # brute force has O(n^2) time complexity since we involve a nested for loop

        min_price = float('inf') # set min price to - infinity because we want it to be such that any number 
        # in the array is bigger than this, so it can be included. Ie., if we set min_price = 0, then chances are 
        # that it will be less than most of the integers in the array, which is not accurate for what we want 
        max_profit = 0 # set max_profit to 0 for now and increase it in the future if we see something bigger 

        for price in prices: # iterate through every number in the array 
            if price < min_price: # if one of the numbers is < -inf 
                min_price = price # update 
            
            profit = price - min_price # find profit by doing this formula 

            if profit > max_profit: # if profit is bigger than max
                max_profit = profit # set max_profit = to the biggest profit 
            
        return max_profit  








            
            