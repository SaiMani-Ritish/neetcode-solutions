class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax = 0
        rightmax = 0
        left = 0 
        right = len(height) - 1
        count = 0

        while left < right:
            leftmax = max(height[left], leftmax)
            rightmax = max(height[right], rightmax)
            if leftmax < rightmax:
                count += leftmax - height[left]
                left += 1
            else:
                count += rightmax - height[right]
                right -= 1
        return count


        