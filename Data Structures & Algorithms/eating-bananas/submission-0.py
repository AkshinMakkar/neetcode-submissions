class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # min bananas is 1 
        l = 1 
        r = max(piles) # max bananas is the largest element in the pile 

        # loop through the array 
        while l < r: 
            mid = (l+r) // 2 # calculate the mid (bananas per hour starting off w l and r)
            hours = 0 
            for bananas in piles: 
              hours += math.ceil(bananas/mid)   # find the number of hours it takes using the current mid 
            if hours > h: # compare between our h constraint and see if its greater 
                l = mid + 1 # if its greater we know the current mid took too long, so we must go higher up (as the more right you get, the shorter the hours get)
            else: # if the amount of hours was either < and =, then we set r = mid, because we don't want to exclude the mid we got as it may turn out to be the minimum number of bananas we can eat in the h constrain 
                r = mid 
        
        return l # when we get r = l return l 
            