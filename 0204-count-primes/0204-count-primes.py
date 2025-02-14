class Solution(object):
    def countPrimes(self, n):
        if n <= 2:
            return 0
    
    # Create a list to track prime status of numbers from 0 to n-1
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
    
        for i in range(2, int(n ** 0.5) + 1):
             if is_prime[i]:
                for j in range(i * i, n, i):
                    is_prime[j] = False
        return sum(is_prime) 
    