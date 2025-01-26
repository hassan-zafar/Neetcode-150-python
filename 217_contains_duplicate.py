# https://leetcode.com/problems/contains-duplicate/
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        num_set = set()  # Create a set to store unique numbers
        
        for num in nums:
            if num in num_set:  # Check if the number already exists in the set
                return True
            else:
                num_set.add(num)  # Add the number to the set if it's not already present
        
        return False