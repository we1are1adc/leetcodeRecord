#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        b = dict(zip(range(l),nums))
        result = sorted(b.items(),key=lambda x : x[1])
        end = l-1
        start = 0
        while result[start][1] + result[end][1] !=target:
            if result[start][1] + result[end][1] < target:
                start+=1
            else:
                end -= 1
        return [result[start][0],result[end][0]]
# @lc code=end
