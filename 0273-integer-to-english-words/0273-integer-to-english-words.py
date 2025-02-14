class Solution(object):
    def numberToWords(self, num):
        if num == 0:
            return "Zero"
        
        # Arrays for word mappings
        less_than_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", 
                         "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]
        
        def helper(n):
            # Convert a number less than 1000 to words
            if n == 0:
                return ""
            elif n < 20:
                return less_than_20[n] + " "
            elif n < 100:
                return tens[n // 10] + " " + helper(n % 10)
            else:
                return less_than_20[n // 100] + " Hundred " + helper(n % 100)
        
        result = ""
        
        # Iterate over the number groups (billions, millions, thousands, ones)
        for i in range(4):  # Billions, Millions, Thousands, Ones
            if num % 1000 != 0:  # Process only if the group is not zero
                result = helper(num % 1000) + thousands[i] + " " + result
            num //= 1000
        
        # Trim trailing spaces and return
        return result.strip()