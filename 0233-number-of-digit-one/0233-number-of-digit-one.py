class Solution(object):
    def countDigitOne(self, n):
        count = 0
        i = 1  # We start with the units place, then tens, hundreds, etc.
    
        while i <= n:
        # Calculate the high, current, and low parts for the current digit place
            high = n // (i * 10)
            current = (n // i) % 10
            low = n % i
        
            if current == 0:
                count += high * i
            elif current == 1:
                count += high * i + low + 1
            else:
                count += (high + 1) * i
        
            i *= 10  # Move to the next digit place (tens, hundreds, etc.)
    
        return count