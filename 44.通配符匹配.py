#
# @lc app=leetcode.cn id=44 lang=python3
#
# [44] 通配符匹配
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
            s_len = len(s)
            p_len = len(p)
            pro = [[False] * (p_len+1) for _ in range(s_len+1)] 
            pro[0][0] = True
            for i in range(1,p_len+1):
                if p[i-1] == "*":
                    pro[0][i] = True
                else:
                    break
            for s_i in range(s_len):
                for p_i in range(p_len):
                    if p[p_i] == "*":
                        pro[s_i+1][p_i+1] = pro[s_i][p_i+1] | pro[s_i+1][p_i]
                    elif p[p_i] == "?" or p[p_i] == s[s_i]:
                        pro[s_i+1][p_i+1] = pro[s_i][p_i]
            return pro[s_len][p_len]
# @lc code=end
