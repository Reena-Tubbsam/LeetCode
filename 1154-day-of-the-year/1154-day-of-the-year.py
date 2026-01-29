class Solution:
    def dayOfYear(self, date: str) -> int:
        # Step 1: Extract year, month, and day
        year, month, day = map(int, date.split('-'))
        
        # Step 2: Days in each month (non-leap year)
        days_in_month = [31, 28, 31, 30, 31, 30,
                         31, 31, 30, 31, 30, 31]
        
        # Step 3: Check if leap year
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            days_in_month[1] = 29  # February
        
        # Step 4: Add days of previous months + current day
        total_days = sum(days_in_month[:month - 1]) + day
        
        return total_days