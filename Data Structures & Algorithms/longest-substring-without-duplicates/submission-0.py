class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window approach (O(n) approach)
        l = 0 # left pointer
        longest = 0 # length
        sett = set() # empty set to store values in, helps with O(1) lookup
        n = len(s) # length of the set 

        for r in range(n): # iterate 
            while s[r] in sett: # if placement of set[r] is in set 
                sett.remove(s[l]) # remove the value at index l in the set
                l += 1 # increment 
        
            w = (r-l) + 1 # length
            longest = max(longest, w) # compare longest length 
            sett.add(s[r]) # add the value at s[r] into the set 

        return longest 

