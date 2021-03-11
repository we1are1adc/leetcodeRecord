#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseLink(self,head:ListNode,n:int)->ListNode:
        if n == 1:
            return head
        # if n == 1:
        last = self.reverseLink(head.next,n-1)
        temp = head.next.next
        head.next.next = head
        head.next = temp
        return last
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        if m == 1:
            last = self.reverseLink(head,n)
            return last
        last = self.reverseBetween(head.next,m-1,n-1)
        head.next = last
        return head

# @lc code=end

