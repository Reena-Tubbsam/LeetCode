class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # If the number of stones is a multiple of 4, you will lose
        # if your opponent also plays optimally.
        return n % 4 != 0