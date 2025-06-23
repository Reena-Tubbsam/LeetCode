class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        #If n is 0 or negative, it fails immediately
        if n <= 0:
            return False
        #Keep dividing by 4 while possible
        while n > 1:
            if n % 4  != 0:
                return False 
            n//=4
        #If we've reached exactly 1, it's good
        return n== 1
        
        