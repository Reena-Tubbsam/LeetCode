class Solution(object):
    def romanToInt(self, s):
       # Step 1: Make a dictionary to know what each symbol means
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0  # This will store the final number
        i = 0      # This is the position we are reading

        # Step 2: Go through the string
        while i < len(s):
            # Step 3: Check if there is a next symbol and it's bigger
            if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
                # This means subtract current from next
                total += values[s[i + 1]] - values[s[i]]
                i += 2  # Skip both symbols
            else:
                # Just add the current symbol
                total += values[s[i]]
                i += 1  # Move to next symbol

        return total