class Solution:
    def findMin(self, nums: List[int]) -> int:

        # binary search 

        length = len(nums)
        left = 0 
        right = length - 1

        while left < right: 
            mid = (left + right) // 2
            # in a rotated array, if the number at mid > then the array than it means the numbers are more greater on the left than right, meaning that the min number is on the right side, which is why we move left to mid + 1 
            if nums[mid] > nums[right]:
                left = mid + 1 
            else: # else, maybe the number at mid is < than the numbers at the right, than it means the numbers on the left are smaller, which is why we set right = mid 
                right = mid 

        return nums[left]
# the left side has the smaller number, so return this 












        #* O(n log n) time -> sorting takes this in the worst case 
        # ex., a = [3,5,4,1] n = len(a) = 4 
        # 3541 -> 35, 41, 3, 5, 4, 1 (takes two times) -> log2(4) = 2 = n 
        # the total growth on this increases like n log n 
        # s = sorted(nums)
        # return s[0]
        # growth is n log n as we are doing n levels work processed/level and log2(8) tells us how many levels we have total, so therefore, n log n time complexity 
