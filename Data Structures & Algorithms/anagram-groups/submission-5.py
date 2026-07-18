class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {} # empty dict to store values 
        for i in strs: # iterate through list 
            if tuple(sorted(i)) in my_dict: # sort i and see if its already in the "database" (dictionary)
                my_dict[tuple(sorted(i))].append(i)  # if it is, add the value to the key which is in sorted form 
            else: # if not 
                my_dict[tuple(sorted(i))] = [i] # add to the dict 

        return list(my_dict.values()) # finalize the return 

# Notes: 
# maybe make a dictionary and group words, and then for every next 
        # word, we iterate through that and cross check? 
        # sort? 

"""
 brute force 
        empty_dict = {}
        for i in strs():
            empty_dict = i
            for r in strs():
                if i == r: 
                    i.r.join()
"""










