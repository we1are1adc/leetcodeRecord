#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        def match(i,j):
            if i == -1:
                return False
            if p[j] == "." or s[i] == p[j]:
                return True
            return False
        memo = [[False] * (m+1) for i in range(n+1)]
        memo[0][0] = True

        for i in range(-1,n):
            for j in range(m):
                if p[j] == "*":
                    memo[i+1][j+1] = memo[i+1][j-1]
                    if match(i,j-1):
                        memo[i+1][j+1] = memo[i][j+1] or memo[i+1][j+1]
                else:
                    if match(i,j):
                        memo[i+1][j+1] = memo[i][j]
        return memo[n][m]
                 

# @lc code=end

