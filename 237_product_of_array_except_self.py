# https://leetcode.com/problems/product-of-array-except-self
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        results = [1] * len(nums)

        pre = 1
        post = 1
        for i in range(len(nums)):
            results[i]=pre
            pre*=nums[i]
        
        for i in range(len(nums)-1,-1,-1):
            results[i]*=post
            post*=nums[i]
        return results