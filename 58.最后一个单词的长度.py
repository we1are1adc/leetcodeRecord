#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        result = s.split(" ")
        for n in range(-1, -1-len(result),-1):
            if len(result[n]) > 0:
                return len(result[n])
            elif n == -len(result):
                return 0
# @lc code=end

