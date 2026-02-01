class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        # Start from the square root of the area
        width = int(area ** 0.5)

        # Move downward to find the first divisor
        while area % width != 0:
            width -= 1

        # Once width is found, length is area // width
        length = area // width

        return [length, width]