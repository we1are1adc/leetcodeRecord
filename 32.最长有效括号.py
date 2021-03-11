#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        len_s = len(s)
        max_to_now = 0
        dp = [0 for _ in range(len(s))]
        for i in range(1,len_s):
            if s[i] == ")":
                if s[i-1] == "(":
                    if i >1 :
                        dp[i] = dp[i-2]+2
                    else:
                        dp[i] = 2
                elif i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == "(":
                        if dp[i-1] > 0:
                            dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]
                        else:
                            dp[i] = 0
                        # dp[i] = (dp[i-dp[i-1]-2] + 2 + dp[i-1]) if i-dp[i-1]-2 >= 0 else (4 + dp[i-1])
                max_to_now = max(max_to_now, dp[i])
        return max_to_now

# @lc code=end

