# Last updated: 2025/10/6 16:24:33
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result_indexes = []
        for out_ind in range(len(nums)):
            out_num = nums[out_ind]
            for in_ind in range(out_ind + 1, len(nums)):
                in_num = nums[in_ind]
                if out_num + in_num == target:
                    result_indexes.append(out_ind)
                    result_indexes.append(in_ind)
                    return result_indexes
        