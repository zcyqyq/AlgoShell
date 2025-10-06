# Last updated: 2025/10/6 16:24:32
class Solution(object):
    def maxArea(self, height):
        left_idx = 0
        right_idx = len(height) - 1
        max_area = (right_idx - left_idx) * min([height[left_idx], height[right_idx]])
        while left_idx < right_idx:
            if height[left_idx] < height[right_idx]:
                left_idx +=1
            else:
                right_idx -=1    
            max_area = max(max_area, (right_idx - left_idx) * min([height[left_idx], height[right_idx]]))
        return max_area
