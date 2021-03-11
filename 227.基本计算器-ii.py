#
# @lc app=leetcode.cn id=227 lang=python3
#
# [227] 基本计算器 II
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        def helper(s):
            stack = []
            i = 0
            currentNum = 0
            sign = "+"
            signNum = 1
            for ii in range(len(s)):
                i = s[ii]
                if i != " ":
                    if i.isdigit():
                        currentNum = currentNum * 10 + int(i)
                    if (not i.isdigit()):
                        if sign == '+':
                            stack.append(currentNum)
                        elif sign == '-':
                            stack.append(-currentNum)
                        elif sign == '*':
                            stack[-1] = stack[-1] * currentNum
                        else:
                        # python 除法向 0 取整的写法
                            stack[-1] = int(stack[-1] / float(currentNum))  
                        currentNum = 0
                        sign = i
                if ii == len(s)-1:
                        if sign == '+':
                            stack.append(currentNum)
                        elif sign == '-':
                            stack.append(-currentNum)
                        elif sign == '*':
                            stack[-1] = stack[-1] * currentNum
                        elif sign == '/':
                        # python 除法向 0 取整的写法
                            stack[-1] = int(stack[-1] / float(currentNum))  
            return sum(stack)
        return helper(list(s))
        
# @lc code=end

