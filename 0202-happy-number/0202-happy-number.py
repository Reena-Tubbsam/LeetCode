class Solution(object):
    def isHappy(self, n):
        def get_sum_of_squares(num):
            return sum(int(digit) ** 2 for digit in str(num))
        
        seen = set()
        
        while n != 1:
            n = get_sum_of_squares(n)
            if n in seen:
                return False
            seen.add(n)
        
        return True