class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # two pointer approach 
        L = 0 
        n = len(numbers)
        R = n - 1 

        while L < R:
            sum = numbers[L] + numbers[R]
            if sum == target:
                return [L+1, R+1]
            elif sum > target:
                    R -= 1
            else:
                L += 1 

        