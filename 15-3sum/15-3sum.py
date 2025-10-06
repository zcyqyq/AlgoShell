# Last updated: 2025/10/6 16:24:31
class Solution(object):
    def threeSum(self, nums):
        res = []
        nums = sorted(nums)
        for i in range(len(nums) - 2):
            target = 0 - nums[i]
            sort_nums = nums[i + 1 : ]
            left = 0
            right = len(sort_nums) - 1
            while left < right:
                if sort_nums[left] + sort_nums[right] == target:
                    triplet = sorted([nums[i], sort_nums[left], sort_nums[right]])
                    if triplet not in res: 
                        res.append(triplet)
                    left += 1
                    right -= 1
                elif sort_nums[left] + sort_nums[right] < target:
                    left += 1
                else:
                    right -= 1
        return res
