#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x > -1 :
            if x < 10:
                return True
            a = x
            b = 0

            while x > 0.99:
                b *= 10
                b +=  x % 10
                x = x//10
            if b == a:
                return True
        return False
# @lc code=end

