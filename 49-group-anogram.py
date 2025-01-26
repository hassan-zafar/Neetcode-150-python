# https://leetcode.com/problems/group-anagrams

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # If the input list is empty, return an empty list
        if not strs:
            return []
        
        # Create a dictionary to store the grouped anagrams
        ans_map = defaultdict(list)  # Default value for missing keys is an empty list
        
        # Iterate through each string in the input list
        for s in strs:
            # Initialize a count array for 26 letters, all set to 0
            count = [0] * 26
            
            # Count the frequency of each character in the string
            for char in s:
                count[ord(char) - ord('a')] += 1
            
            # Convert the count array to a unique key (using a tuple as it's hashable)
            
            # Add the string to the appropriate group in the dictionary
            ans_map[tuple(count)].append(s)
        
        # Return all the grouped anagrams as a list of lists
        return list(ans_map.values())
