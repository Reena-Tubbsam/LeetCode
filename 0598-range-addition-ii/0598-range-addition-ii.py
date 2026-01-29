class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        # If there are no operations,
        # all cells are equal (all are 0)
        if not ops:
            return m * n
        
        # Start with maximum possible limits
        min_row = m
        min_col = n
        
        # Find the smallest ai and bi
        for a, b in ops:
            min_row = min(min_row, a)
            min_col = min(min_col, b)
        
        # The overlapping area gives the count of max integers
        return min_row * min_col