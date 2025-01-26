class Solution:
    def twosum(self,nums=list[int],target=int)-> list[int]:
        num_map = {}
        for i, num in enumerate(nums):
            if target - num in num_map:
                return [num_map[target - num], i]
            num_map[num] = i
