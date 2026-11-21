class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True 
        else:
            return False
        
# time complexity is O(n log n)
