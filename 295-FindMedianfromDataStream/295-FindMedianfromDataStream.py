# Last updated: 2025/10/7 17:46:01
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        left = -1
        right = -1
        res = []
        intervals = sorted(intervals)
        for interval in intervals:
            if right < interval[0]:
                # if not initial value
                if left != -1:
                    res.append([left, right])
                left = interval[0]
                right = interval[1]
                continue
            if interval[0] >= left and interval[0] <= right:
                if interval[1] > right:
                    right = interval[1]
                    continue
        res.append([left, right])
        return res
        