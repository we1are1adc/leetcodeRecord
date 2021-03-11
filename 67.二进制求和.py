#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a == '0':
            return b
        elif b == "0":
            return a
        else:
            value_a = 0 
            value_b = 0
            for a_i in a:
                value_a = value_a*2 + int(a_i)
            for b_i in b:
                value_b = value_b*2 + int(b_i)
            value = value_a +  value_b
            v = ''
            while value > 0:
                v =  "%d" % (value%2) + v
                value = value//2
            # v = v + "%d" % value
            return v
# @lc code=end

