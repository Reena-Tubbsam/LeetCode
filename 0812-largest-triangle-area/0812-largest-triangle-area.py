class Solution(object):
    def largestTriangleArea(self, points):
        # This function calculates the area of a triangle formed by three points
        def calculate_area(p1, p2, p3):
            x1, y1 = p1
            x2, y2 = p2
            x3, y3 = p3

            # Using the triangle area formula (Shoelace formula)
            area = abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2.0
            return area

        n = len(points)
        max_area = 0  # To store the largest area found

        # Check all combinations of 3 different points
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    # Pick three different points
                    point1 = points[i]
                    point2 = points[j]
                    point3 = points[k]

                    # Calculate area of triangle formed by these three points
                    area = calculate_area(point1, point2, point3)

                    # Update max_area if we found a bigger one
                    if area > max_area:
                        max_area = area

        return max_area
            