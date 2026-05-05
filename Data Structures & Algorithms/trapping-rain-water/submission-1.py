class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax = 0
        rightmax = 0
        left = 0
        right = len(height) - 1
        water = 0

        while left < right:
            leftmax = max(height[left], leftmax)
            rightmax = max(height[right], rightmax)
            if height[left] < height[right]:
                water += leftmax - height[left]
                left += 1
            else:
                water += rightmax - height[right]
                right -= 1
        return water 
        