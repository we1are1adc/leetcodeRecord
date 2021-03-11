#
# @lc app=leetcode.cn id=354 lang=python3
#
# [354] 俄罗斯套娃信封问题
#

# @lc code=start
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        envelopes.sort(key=lambda x:(x[0],-x[1]))
        N = len(envelopes)
        dp = [1] *N
        for i in range(N):
            for j in range(i):
                if envelopes[j][1] < envelopes[i][1]:
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)
# @lc code=end

