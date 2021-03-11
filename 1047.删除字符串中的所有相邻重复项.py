#
# @lc app=leetcode.cn id=1047 lang=python3
#
# [1047] 删除字符串中的所有相邻重复项
#

# @lc code=start
class Solution:

    def removeDuplicates(self, s: str) -> str:

        if len(s) < 2:
            return s
        result = s[0]
        for i in s[1:]:
            if len(result) < 1:
                result += i
            elif  not result[-1] == i:
                result += i
            else:
                result = result.rsplit(i,1)[0]
        return result
# @lc code=end

