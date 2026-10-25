class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]  
            if slow == fast:
                break

        two_slow = 0
        while True:
            slow = nums[slow]
            two_slow = nums[two_slow]
            if slow == two_slow:
                return slow

        
