# Last updated: 2025/10/6 16:24:29
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(len(s)):
            for word in wordDict:
                if len(word) > i + 1:
                    continue
                substr = s[i + 1 - len(word) : i + 1]
                dp[i + 1] = (substr == word) and dp[i + 1 - len(word)]
                if dp[i + 1]:
                    break
        return dp[-1]