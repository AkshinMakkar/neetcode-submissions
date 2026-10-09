class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stkk = []
        largest_area = 0 

        for index, height in enumerate(heights):
            start = index 
            while stkk and height < stkk[-1][0]:
                h, j = stkk.pop()
                w = index - j
                a = h * w
                largest_area = max(largest_area, a)
                start = j 
            stkk.append((height, start))
                
        while stkk: 
            h, j = stkk.pop()
            w = n - j 
            largest_area = max(largest_area, h*w)
        
        return largest_area


