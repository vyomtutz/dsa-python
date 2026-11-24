#Input

nums = [1, 2, 3, 1, 2, 3]

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # Create a set to store unique elements
        seen = set()
        
        # Iterate through each number in the list
        for num in nums:
            # If the number is already in the set, return True
            if num in seen:
                return True
            # Otherwise, add the number to the set
            seen.add(num)
        
        # If no duplicates were found, return False
        return False