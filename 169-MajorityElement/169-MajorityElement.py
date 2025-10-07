# Last updated: 2025/10/7 15:32:10
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        return nums[len(nums) // 2]
        