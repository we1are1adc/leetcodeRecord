#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        l = [1]
        if n == 1:
            return str(n)
        for i in range(1,n):
            stack = []
            for s in l:
                if len(stack) < 2:
                    stack.append(1)
                    stack.append(s)
                elif stack[-1] != s:
                    stack.append(1)
                    stack.append(s)
                else:
                    stack[-2] += 1
            l = stack
        l = [str(_) for _ in l]
        return ''.join(l)
                


            
# @lc code=end

