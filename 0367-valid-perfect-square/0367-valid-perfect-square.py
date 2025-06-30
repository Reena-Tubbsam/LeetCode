class Solution(object):
    def isPerfectSquare(self, num):
    #Use the property that 1 + 3 + 5 + … + (2k−1) = k². 
    #Returns True if n is a perfect square by subtracting odd numbers
        odd = 1
        while num > 0:
            num -= odd
            odd += 2
        return num == 0