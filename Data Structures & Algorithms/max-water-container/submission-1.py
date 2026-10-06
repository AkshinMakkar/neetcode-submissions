class Solution:
    def maxArea(self, heights: List[int]) -> int:

        n = len(heights)
        f = 0 
        l = n - 1 

        max_area = 0 
        
        while f < l: 
            curr_height = min(heights[f], heights[l])
            curr_width = l - f 
            a = curr_height * curr_width
            max_area = max(max_area, a)
            
            if heights[f] < heights[l]:
                f += 1
            else:
                l -= 1

        return max_area

            

        



        

            
