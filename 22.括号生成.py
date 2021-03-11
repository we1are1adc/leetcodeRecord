#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def backtrack(route,num):
            if len(route) == n*2:
                result.append(route)
                return

            if len(route) - (n - num) < (n - num):
                route += ")"
                backtrack(route,num)
                route = route[0:len(route)-1]
            if num > 0:
                route += "("
                backtrack(route,num-1)
                route = route[0:len(route)-1]
        backtrack("(",n-1)
        return result
# @lc code=end

