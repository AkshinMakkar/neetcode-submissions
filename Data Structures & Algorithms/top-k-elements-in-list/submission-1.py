# comments added
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    
    # step 1, make an empty hash map and count the number of repeated instances of the same value 
        count = {}
        for num in nums: 
            count[num] = count.get(num, 0) + 1 

# step 2, make a list for every value up to the row of the max frequency (len(nums) + 1)
# add the numbers to each value at the respective frequency 
        bucket = [[] for j in range(len(nums) + 1)]
        for num, freq in count.items():
            bucket[freq].append(num)
        
        # Step 3: empty result list 
        # back track from frequency in bucket, and add to list 
        # if we are greater or = to K, then return that resulting list 
        result = []
        for i in range(len(bucket) - 1, 0, -1):
            result.extend(bucket[i])
            if len(result) >= k:
                return result[:k]


















