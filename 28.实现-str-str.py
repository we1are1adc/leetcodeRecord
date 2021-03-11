#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        hl = len(haystack)
        nl = len(needle)
        if nl == 0:
            return 0
        for i in range(hl-nl+1):
            if haystack[i] == needle[0]:
                for i2 in range(0,nl):
                    if needle[i2] != haystack[i+i2]:
                        break
                    if i2 == nl-1:
                        return i
        return -1
# @lc code=end

