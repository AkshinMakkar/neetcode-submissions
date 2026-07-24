class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointer approach 
        n = len(s) # get the length of the string 
        L = 0 # first position 
        R = n - 1 # last position 

        while L < R:
            if not s[L].isalnum(): # confirm if the position is a number or not 
                L += 1 # increment by 1 
                continue 

            if not s[R].isalnum(): 
                R -= 1 
                continue 
            
            if s[L].lower() != s[R].lower():
                return False 
                
            
            L += 1 
            R -= 1 

        return True 









        
        