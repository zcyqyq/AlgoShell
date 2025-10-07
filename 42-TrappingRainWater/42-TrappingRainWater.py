# Last updated: 2025/10/7 16:27:58
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n
        max_right[n - 1] = height[n - 1]
        rain = 0
        for i in range(n):
            max_left[i] = max(height[i], max_left[i - 1])
        for i in range(n - 2, -1, -1):
            max_right[i] = max(height[i], max_right[i + 1])
        for i in range(n):
            h = min(max_left[i], max_right[i])
            rain += (h - height[i])
        return rain

