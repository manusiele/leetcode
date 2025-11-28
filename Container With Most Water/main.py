class Solution(object):
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            # Calculate current area
            width = right - left
            area = min(height[left], height[right]) * width
            max_area = max(max_area, area)

            # Move pointer of smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
