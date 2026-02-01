class Solution:
    def arrangeCoins(self, n: int) -> int:
        coins_used = 0   # total coins used so far
        row = 0          # current completed rows

        # keep building rows while we have enough coins
        while coins_used + (row + 1) <= n:
            row += 1
            coins_used += row

        return row