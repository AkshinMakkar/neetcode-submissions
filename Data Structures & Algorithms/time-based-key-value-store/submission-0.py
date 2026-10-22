class TimeMap:

    def __init__(self):
        # initialize a empty hash map, with a key mapped to a list of lists -> the value and timestamp 
           self.store = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        # if the keys do not exist in the hash map, store a list at that key 
        # ie., ["bob", "happy", 1] does not exist: make {bob: []}
        if key not in self.store:
            self.store[key] = []
        # if we already have a key to list pair, add the [value, timestamp] at the end of the list. For example, we now have bob: [], so if we have ("Bob", "Mad", 2), we will add {bob: [[Mad, 2]]} to the end of the list 
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        result = "" # if the key does not exist, return the empty string 
        # get the list at that key, and if it does not exist, return an empty list 
        list_of_values = self.store.get(key, [])

        # now binary search: 
        left = 0 
        right = len(list_of_values) - 1 

        # iterate 
        while left <= right:
            mid = (left+right) // 2
            if list_of_values[mid][1] <= timestamp: # we use list_of_values[mid][1] because we want to look at the timestamp, which is at index 1 
                result = list_of_values[mid][0] # if it is, set result = to this 
                left = mid + 1 
            else:
                right = mid - 1
        
        return result 


            
        
        
            
