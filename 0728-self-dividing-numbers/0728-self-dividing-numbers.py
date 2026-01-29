class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []  # To store all self-dividing numbers
        
        # Check each number in the range
        for num in range(left, right + 1):
            
            temp = num      # Copy of num for digit checking
            is_valid = True
            
            # Extract digits one by one
            while temp > 0:
                digit = temp % 10
                
                # If digit is 0 or does not divide the number
                if digit == 0 or num % digit != 0:
                    is_valid = False
                    break
                
                temp //= 10  # Remove last digit
            
            # If all digits passed the test
            if is_valid:
                result.append(num)
        
        return result