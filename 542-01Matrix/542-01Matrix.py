# Last updated: 2025/10/6 18:56:00
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        # First, 1-dim dp with no reverse order
        # but need to record
        dp = [[] for _ in range(target + 1)]
        dp[0] = [[]]
        for i in range(len(candidates)):
            for j in range(candidates[i], target + 1):
                for comb in dp[j - candidates[i]]:
                    dp[j].append(comb + [candidates[i]])
        return dp[target]
        