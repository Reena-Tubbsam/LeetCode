class Solution:
    def toHex(self, num: int) -> str:
    
        if num == 0:
            return "0"
        
        # handle negative numbers using 32-bit two's complement
        if num < 0:
            num += 2 ** 32
        
        digits = "0123456789abcdef"
        result = ""
        
        while num > 0:
            remainder = num % 16
            result = digits[remainder] + result
            num //= 16
        
        return result
    