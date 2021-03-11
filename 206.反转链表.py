#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 迭代
        if head == None or head.next == None:
            return head
        head_temp = head
        head_new = ListNode(head.val)
        while head_temp.next != None:
            temp = ListNode(head_temp.next.val)
            temp.next = head_new
            head_new = temp
            head_temp = head_temp.next
        return head_new
        # 递归
        # if head == None or head.next == None:
        #     return head
        # last = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return last
# @lc code=end

