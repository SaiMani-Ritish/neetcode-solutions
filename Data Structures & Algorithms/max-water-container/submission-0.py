class Solution:
    def maxArea(self, heights: List[int]) -> int:
        most_water = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            bar_height = min(heights[left], heights[right])
            width = right - left
            area = bar_height * width
            most_water = max(most_water, area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return most_water
            
        
        