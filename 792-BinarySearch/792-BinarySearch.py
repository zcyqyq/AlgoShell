# Last updated: 2025/10/6 16:24:30
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            next_idx = left + int((right - left) / 2)
            if target > nums[next_idx]:
                left = next_idx + 1
            elif target < nums[next_idx]:
                right = next_idx - 1
            else:
                return next_idx
        return -1

        