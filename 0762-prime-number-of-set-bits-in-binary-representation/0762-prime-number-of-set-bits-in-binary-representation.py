class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
       # Step 1: Store all prime numbers we might need
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        
        count = 0  # This will store our final answer
        
        # Step 2: Go through every number in the range
        for num in range(left, right + 1):
            
            # Step 3: Convert number to binary and count '1's
            set_bits = bin(num).count('1')
            
            # Step 4: Check if set_bits is prime
            if set_bits in primes:
                count += 1
        
        # Step 5: Return the result
        return count 