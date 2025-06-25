class Solution(object):
    def mySqrt(self, x):
        # Special cases for 0 and 1
        if x == 0 or x == 1:
            return x

    # Start from 1 and go up to x // 2
        i = 1
        while i * i <= x:
            i += 1  # Keep going until square is more than x

        return i - 1  # Step back once because i*i went over x