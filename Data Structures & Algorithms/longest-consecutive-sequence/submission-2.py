class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums) # convert to a set to make O(1) and avoid duplicates 
        longest = 0 # we haven't seen anything yet, set longest = 0 for now 
        
        # iterate through every number in the array
        for num in nums: 
            if num - 1 not in s: 
                num_next = num + 1 
                length = 1 
                while num_next in s:
                    length += 1 
                    num_next += 1 
                longest = max(longest, length)
        
        return longest