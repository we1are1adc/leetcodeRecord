#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start
class Solution:
    # 法一 dp[n]表示以nums[n]为结尾的最长序列 略
    # 法二 dp[n]表示长度为n的最长递增子序列的最大值
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        dp = [0] * n
        dp[0] = nums[0]
        max_result = 1
        for i in range(1, n):
            r = max_result
            for j in range(r - 1, -1, -1):
                if dp[j] < nums[i]:
                    dp[j + 1] = nums[i]
                    max_result = max(j + 2, max_result)
                    break
                if j == 0:
                    dp[j] = nums[i]
        return max_result
            
# @lc code=end

