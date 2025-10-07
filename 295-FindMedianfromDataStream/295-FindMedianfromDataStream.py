# Last updated: 2025/10/7 16:57:59
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        used  = [False] * len(nums)
        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                path = path + [nums[i]]
                used[i] = True
                backtrack(path)
                path.pop()
                used[i] = False
        backtrack([])
        return res
            
        