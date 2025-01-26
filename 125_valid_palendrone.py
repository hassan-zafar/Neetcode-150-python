# https://leetcode.com/problems/valid-palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1  # Initialize pointers at the start and end of the string
        
        while left < right:
            # Move the left pointer forward if it's not a letter or digit
            while left < right and not s[left].isalnum():
                left += 1
            
            # Move the right pointer backward if it's not a letter or digit
            while left < right and not s[right].isalnum():
                right -= 1
            
            # Check if characters are not equal (case insensitive)
            if s[left].lower() != s[right].lower():
                return False
            
            # Move pointers closer for the next comparison
            left += 1
            right -= 1
        
        return True  # If no mismatch is found, it's a palindrome
