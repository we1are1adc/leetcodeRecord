#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = len(nums)
        if target > nums[-1]:
            return l
        for i in range(l):
            if target <= nums[i]:
                return i


# @lc code=end

