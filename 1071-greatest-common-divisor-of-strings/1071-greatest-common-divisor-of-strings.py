class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Find the shorter string
        min_len = min(len(str1), len(str2))
        
        # Try each prefix (from longest to shortest)
        for i in range(min_len, 0, -1):
            prefix = str1[:i]
            
            # Check if prefix divides both str1 and str2
            if self.isDivisible(str1, prefix) and self.isDivisible(str2, prefix):
                return prefix
        
        return ""
    
    def isDivisible(self, s, prefix):
        # Check if s can be made by repeating prefix
        repeat_count = len(s) // len(prefix)
        if prefix * repeat_count == s:
            return True
        else:
            return False