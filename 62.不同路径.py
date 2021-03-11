#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        
        for _ in range(m):
            dp[_][0] = 1 
        for _ in range(n):
            dp[0][_] = 1 

        for m_i in range(1,m):
            for n_i in range(1,n):
                dp[m_i][n_i] = dp[m_i-1][n_i] + dp[m_i][n_i-1]
        return dp[m-1][n-1]
# @lc code=end

