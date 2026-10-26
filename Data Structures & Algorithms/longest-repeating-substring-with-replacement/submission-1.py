class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window: 
        i = 0 # start at 0 
        count = {} # hash map to keep track of the amount of times we see a value
        max_count = 0 # we will use this to help keep track of the max count 
        longest = 0 # the longest substring we return with the one distinct character 
        n = len(s)


        # move along the string 
        for j in range(n):
            # go through every value, and if it's new, start at 0, and if not, add it by 1 
            count[s[j]] = count.get(s[j], 0) + 1
            max_count = max(max_count, count[s[j]])

                # sliding window to make sure we are below k
            while(j - i + 1) - max_count > k:
                count[s[i]] -= 1
                i += 1 
            
            # return it when we are in the right limit 
            longest = max(longest, j - i + 1)

        return longest
            


            
            


        
        
        
        

        
                


