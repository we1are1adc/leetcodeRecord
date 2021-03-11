#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        if obstacleGrid[0][0] == 1:
            return 0
        dp[0][0] = 1
        for _ in range(1,m):
            if obstacleGrid[_][0]  == 1:    
                dp[_][0] = 0
            else:
                dp[_][0] = min(dp[_-1][0],1)
            
        for _ in range(1,n):
            if obstacleGrid[0][_]  == 1:    
                dp[0][_] = 0
            else:
                dp[0][_] = min(dp[0][_-1],1)

        for m_i in range(1,m):
            for n_i in range(1,n):
                if obstacleGrid[m_i][n_i] == 1:
                    dp[m_i][n_i] = 0
                else:
                    dp[m_i][n_i] = dp[m_i-1][n_i] + dp[m_i][n_i-1]
        return dp[m-1][n-1]
# @lc code=end

