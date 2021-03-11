#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        le = len(s)
        ans = ''
        beiwang = [[False] * le for _ in range(le)]
        for l in range(le):
            for i in range(le):
                j = i+l
                if j >= le:
                    break
                if l == 0:
                    beiwang[i][j] = True
                elif l == 1:
                    beiwang[i][j] = s[i] == s[j]
                else :
                    beiwang[i][j] = (beiwang[i + 1][j - 1] and s[i] == s[j])
                if beiwang[i][j] and l + 1 > len(ans):
                    ans = s[i:j+1]

        return ans

# @lc code=end

