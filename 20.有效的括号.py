#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        left = ["{","(","["]
        left_key = {"{":1,"(":2,"[":3}
        right =  ["}",")","]"]
        right_key = {"}":1,")":2,"]":3}
        l = []
        for s1 in s:
            if s1 in left:
                l.append(s1)
            elif s1 in right:
                if l and left_key[l[-1]]==right_key[s1]:
                    l.pop()
                else:
                    l.append("ss")
                    break
        return True if len(l)== 0 else False

# @lc code=end

