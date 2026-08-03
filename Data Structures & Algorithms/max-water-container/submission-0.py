class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # two pointer approach
        # Area = Height x Width 
        n = len(heights) # find the height
        L = 0 # left pointer, used at index 0 
        R = n - 1 # right pointer, used at the last index 
        max_area = 0 # tracker for the max area 

        while L < R: # loop until we disatisfy this conditions 
            w = R - L # width is the difference between the right and left pointer index (ie., [2, 3, 4], width(2, 4) = 2 (2-0))
            h = min(heights[L], heights[R]) # height is the shortest between the two bars we are at 
            a = w * h # area formula, width * height 
            max_area = max(max_area, a) # max area comparison 

            if heights[L] < heights[R]: # we want to move on with the highest height, this is the comparison 
                L+=1
            
            else:
                R-=1

        return max_area
