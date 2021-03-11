#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for _ in range(1,m):
            dp[_][0] = grid[_][0] + dp[_-1][0]
        for _ in range(1,n):
            dp[0][_] = grid[0][_] + dp[0][_-1]

        for m_i in range(1,m):
            for n_i in range(1,n):
                dp[m_i][n_i] = min(dp[m_i-1][n_i],dp[m_i][n_i-1]) + grid[m_i][n_i]

        return dp[m-1][n-1]

# @lc code=end

