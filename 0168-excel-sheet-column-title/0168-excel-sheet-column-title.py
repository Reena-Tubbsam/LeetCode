class Solution(object):
    def convertToTitle(self, columnNumber):
        #step one store an empty string
        result = ""
        #step 2 while loop to reapat the process
        while columnNumber > 0:
            columnNumber -= 1  # Shift to 0-based index (This is a trick to make our math easier because Excel starts at 1 (A = 1), but our alphabet starts at 0)

            remainder = columnNumber % 26 #This tells us which letter to use.

            '''(Turn the number into a letter)
            function called chr() to convert a number into a letter.
            chr(65) is 'A', so if remainder = 1, then chr(65 + 1) is 'B'
            Add this letter to the front of our result(Because the last letters are calculated first, we add them to the front.)'''

            result = chr(65 + remainder) + result  # Prepend the corresponding letter
            columnNumber //= 26  # Move to the next digit
            
        return result
        