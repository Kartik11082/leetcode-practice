class Solution:
    def maxArea(self, height: List[int]) -> int:
        localMaxArea, globalMaxArea = 0, 0
        left, right = 0, len(height) - 1
        
        while left < right:
            localMaxArea = min(height[left], height[right]) * (right - left)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
                
            globalMaxArea = max(localMaxArea, globalMaxArea)
        return globalMaxArea