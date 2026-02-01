class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # Perfect numbers must be greater than 1
        if num <= 1:
            return False

        divisor_sum = 1  # 1 is always a divisor

        # Check divisors up to sqrt(n)
        i = 2
        while i * i <= num:
            if num % i == 0:
                divisor_sum += i

                # Add the paired divisor if it's different
                if i != num // i:
                    divisor_sum += num // i
            i += 1

        return divisor_sum == num