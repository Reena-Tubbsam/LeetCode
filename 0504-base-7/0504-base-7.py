class Solution:
    def convertToBase7(self, num: int) -> str:
        # Special case
        if num == 0:
            return "0"

        # Check if the number is negative
        is_negative = num < 0
        num = abs(num)

        result = ""

        # Convert to base 7
        while num > 0:
            remainder = num % 7
            result = str(remainder) + result
            num //= 7

        # Add minus sign if needed
        if is_negative:
            result = "-" + result

        return result