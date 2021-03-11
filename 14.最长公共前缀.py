
#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        end = True
        l = len(strs)
        if strs:
            s = strs[0]
            if s:
                # l = [len(str)for str in strs]
                while end and i < len(s):
                    temp_com = s[i]
                    num = 0
                    for str1 in strs:
                        if i == len(str1) or str1[i] != temp_com:
                            end = False
                            break
                        else:
                            num += 1
                    if l == num:
                        i += 1   
                return '' if i == 0 else s[0:i]
            else:
                return ''
        else:
            return ''

# @lc code=end
