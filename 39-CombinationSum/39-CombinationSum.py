# Last updated: 2025/10/6 19:17:39
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        # First, 1-dim dp with no reverse order
        # but need to record
        # easy but consume large memory
        # dp = [[] for _ in range(target + 1)]
        # dp[0] = [[]]
        # for i in range(len(candidates)):
        #     for j in range(candidates[i], target + 1):
        #         for comb in dp[j - candidates[i]]:
        #             dp[j].append(comb + [candidates[i]])
        # return dp[target]

        # try dfs
        graph = defaultdict(list)
        for i in range(target + 1):
            for j in range(len(candidates)):
                if i + candidates[j] <= target:
                    graph[i].append(i + candidates[j])
        res = []
        def dfs(node, path, start):
            if node == target:
                res.append(path)
                return
            for idx in range(start, len(candidates)):
                num = candidates[idx]
                if node + num <= target:
                    dfs(node + num, path + [num], idx) 
        dfs(0, [], 0)
        return res
            