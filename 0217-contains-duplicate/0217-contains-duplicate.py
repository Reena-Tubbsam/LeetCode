class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()  # Create an empty set to track seen elements
    
        for num in nums:
            if num in seen:  # Check if the number is already in the set
                return True  # Duplicate found
            seen.add(num)  # Add the number to the set
    
        return False  # No duplica