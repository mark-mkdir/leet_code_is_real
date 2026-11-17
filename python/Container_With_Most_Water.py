class Solution(object):
    def maxArea(self, height):
        max_water = 0
        right = len(height) - 1
        left = 0
        while left < right:
            cur_water = min(height[left], height[right]) * (right  -left)
            max_water = max(max_water, cur_water)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water
            

        