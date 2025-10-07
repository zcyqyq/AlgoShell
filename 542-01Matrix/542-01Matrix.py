# Last updated: 2025/10/6 18:36:13
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
            next_idx = left + (right - left) // 2
            if nums[left] <= nums[next_idx]:
                if target > nums[next_idx] or target < nums[left]:
                    left = next_idx + 1
                    continue
                right = next_idx
                next_idx = left + (right - left) // 2
                if target > nums[next_idx]:
                    left = next_idx + 1
                elif target < nums[next_idx]:
                    right = next_idx - 1
                else:
                    return next_idx
            else:
                if target > nums[right] or target < nums[next_idx]:
                    right = next_idx - 1
                    continue
                left = next_idx
                next_idx = left + (right - left) // 2
                if target > nums[next_idx]:
                    left = next_idx + 1
                elif target < nums[next_idx]:
                    right = next_idx - 1
                else:
                    return next_idx
        return -1