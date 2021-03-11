#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        map_roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        i = 0
        str_len = len(s)
        str_list = [s[0]]
        sums = 0
        while  True:
            i += 1
            if i == str_len: 
                if len(str_list) > 1:
                    sums += map_roman[str_list[1]] - map_roman[str_list[0]]
                else:
                    sums += map_roman[str_list[0]]
                break
            else:
                if len(str_list) > 1:
                    sums += map_roman[str_list[1]] - map_roman[str_list[0]]
                    str_list.pop()
                    str_list.pop()
                elif  map_roman[str_list[0]] >=  map_roman[s[i]]:
                    sums += map_roman[str_list[0]]
                    str_list.pop()
            str_list.append(s[i])
        return sums
# @lc code=end