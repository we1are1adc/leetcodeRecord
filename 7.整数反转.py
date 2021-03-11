#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        positive = True
        if x < 0:
            x = -x
            positive = False
        strNum = list(str(x))
        strNum.reverse()
        strNum = ''.join(strNum)
        x_rev = int(strNum)
        if not positive:
            x_rev = -x_rev
        if x_rev > (pow(2,31)-1) or x_rev < - pow(2,31):
            x_rev = 0

        return x_rev

        
# @lc code=end
