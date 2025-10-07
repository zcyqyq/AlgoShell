# Last updated: 2025/10/6 17:42:37
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # First, sort this array in ascending order
        # If we can partite one set to two subsets with equal sum, 
        # what we need to do is to find a subset
        # which can satisfy its sum equals to sum(set) / 2.
        # In this way, change the problem to find some numbers 
        # able to beadded to target sum
        # Use dp: dp[i][v] = dp[i-1][v - value(i)] if nums[i+1] is picked
        #         dp[i][v] = dp[i-1][v] if nums[i+1] is not picked

        is_picked = [0] * len(nums)
        sum_set = sum(nums)
        if sum_set % 2 != 0:
            return False
        else:
            target = sum_set / 2
            dp = [[False for _ in range(target + 1)] for _ in range(len(nums) + 1)]
        for i in range(len(nums) + 1):
            dp[i][0] = True
        for i in range(1, len(nums) + 1):
            for v in range(target + 1):
                if v >= nums[i - 1]:
                    dp[i][v] = dp[i - 1][v - nums[i - 1]] or dp[i - 1][v]
                else:
                    dp[i][v] = dp[i - 1][v]
        return dp[-1][target]

        