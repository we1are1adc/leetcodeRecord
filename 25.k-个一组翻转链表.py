#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseLink(self,head:ListNode,n:int)->ListNode:
        if n < 2:
            return head
        # if n == 1:
        last = self.reverseLink(head.next,n-1)
        temp = head.next.next
        head.next.next = head
        head.next = temp
        return last
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1 or head is None:
            return head
        index = 1
        temp = head
        while index < k:
            temp = temp.next
            if temp is None:
                return head
            index += 1
        last = self.reverseLink(head,k)
        head.next = last
        self.reverseKGroup(last,k)
        # temp.next = last2
        return last

            
# @lc code=end

