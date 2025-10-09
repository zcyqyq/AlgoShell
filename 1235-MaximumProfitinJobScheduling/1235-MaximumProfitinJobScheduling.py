# Last updated: 2025/10/9 13:47:25
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # bubble sort
        # n = len(nums)
        # for i in range(n - 1):
        #     for j in range(i, n):
        #         if nums[i] > nums[j]:
        #             tmp = nums[i]
        #             nums[i] = nums[j]
        #             nums[j] = tmp
            
        # merge sort
        def merge(left, right):
            left_idx = 0
            right_idx = 0
            res = [0] * (len(left) + len(right))
            idx = 0
            while left_idx < len(left) or right_idx < len(right):
                if left_idx == len(left):
                    res[idx:] = right[right_idx:]
                    break
                if right_idx == len(right):
                    res[idx:] = left[left_idx:]
                    break
                if left[left_idx] < right[right_idx]:
                    res[idx] = left[left_idx]
                    left_idx += 1
                else:
                    res[idx] = right[right_idx]
                    right_idx += 1
                idx += 1
            return res
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = merge_sort(arr[0:mid])
            right = merge_sort(arr[mid:])
            return merge(left, right)  
            
        nums[:] = merge_sort(nums)      
        