# https://leetcode.com/problems/3sum/description/

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()  # Step 1: Sort the array
        results = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicate elements for `i`
            if nums[i] > 0:
                break  # Since the array is sorted, there's no way to get a sum of 0

            left, right = i + 1, len(nums) - 1  # Two-pointer initialization
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum < 0:
                    left += 1  # Increase sum by moving left pointer
                elif current_sum > 0:
                    right -= 1  # Decrease sum by moving right pointer
                else:
                    results.append([nums[i], nums[left], nums[right]])  # Store valid triplet
                    
                    # Skip duplicates for `left`
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    
                    # Skip duplicates for `right`
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # Move pointers after processing a valid triplet
                    left += 1
                    right -= 1

        return results
