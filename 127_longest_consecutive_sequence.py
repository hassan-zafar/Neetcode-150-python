# https://leetcode.com/problems/longest-consecutive-sequence/
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0  # If the array is empty, return 0
        
        num_set = set(nums)  # Convert the array to a set for O(1) lookups
        longest_sub = 0  # Variable to store the length of the longest sequence
        
        for num in num_set:
            # Only start counting from the beginning of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_sub = 1  # Current sequence length
                
                # Check for the next consecutive numbers
                while current_num + 1 in num_set:
                    current_num += 1
                    current_sub += 1
                
                # Update the longest sequence length
                longest_sub = max(longest_sub, current_sub)
        
        return longest_sub
