#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = len(nums)
        end = True
        _ = 0 
        while _ < l-1:
            if nums[_] == nums[_+1]:
                nums.remove(nums[_])
                l -= 1
            else:
                _ += 1 

            
        return l
# @lc code=end

