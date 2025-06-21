class Solution(object):
    def addDigits(self, num):
        # Continue until num is a single digit
        while num>=10:
            total =  0
            for digits in str(num):
                total += int(digits)
            num= total
        return num
        