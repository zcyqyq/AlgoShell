# Last updated: 2025/10/9 17:06:18
class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        # sort by start time
        # correct but create a very long dp
        # out of memory

        # indexes = sorted(range(len(startTime)), key=lambda i : startTime[i])
        # t = max(endTime)
        # dp = [0] * t
        # p = t - 1
        # for i in range(len(indexes) - 1, -1, -1):
        #     job_s = startTime[indexes[i]] - 1
        #     job_e = endTime[indexes[i]] - 1
        #     job_pf = profit[indexes[i]]
        #     if job_e > p:
        #         dp[job_s] = max(dp[job_e] + job_pf, dp[p], dp[job_s])
        #     else:
        #         dp[job_s] = max(dp[p] + job_pf, dp[job_s])
        #     for j in range(job_s + 1, p):
        #         dp[j] = dp[p]
        #     p = job_s
        # for i in range(0, p):
        #     dp[i] = dp[p]
        # return dp[0]

        # sort by end time
        indexes = sorted(range(len(endTime)), key=lambda i : endTime[i])
        dp = [0] * (len(profit) + 1)
        t = max(endTime)
        sort_endTime = [endTime[i] for i in indexes]
        p = 0
        for i in range(len(indexes)):
            job_s = startTime[indexes[i]]
            job_e = endTime[indexes[i]]
            job_pf = profit[indexes[i]]
            if job_s < p:
                prev = bisect_right(sort_endTime, job_s) + 1
                dp[i + 1] = max(dp[i], dp[prev - 1] + job_pf)
            else:
                dp[i + 1] = dp[i] + job_pf
            p = job_e
        return dp[-1]

