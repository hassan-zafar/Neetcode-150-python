# https://leetcode.com/problems/container-with-most-water/
class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area=0
        left,right=0,len(height)-1
        while left<right:
            width=right-left
            length=min(height[left],height[right])
            max_area=max(max_area,width*length)

            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        return max_area