#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for n in range(-1,-1-len(digits),-1):
            num += digits[n] * 10**(-1-n)
        num += 1
        l = []
        while num != 0:
            l.append(num%10)
            num = num//10
        l.reverse()
        return l
# @lc code=end

