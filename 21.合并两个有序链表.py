#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # temp1 = l1
        # temp2 = 0
        nodeStart = ListNode()
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val >l2.val:
            nodeStart.val = l2.val
            l2 = l2.next
        else:
            nodeStart.val = l1.val
            l1 = l1.next
        temp = ListNode()
        nodeStart.next = temp
        while True:
            if l1:
                if l2:
                    if l1.val >l2.val:
                        temp.val = l2.val
                        l2 = l2.next
                        temp2 = ListNode()
                        temp.next = temp2
                        temp = temp.next
                    else:
                        temp.val = l1.val
                        l1 = l1.next
                        temp2 = ListNode()
                        temp.next = temp2
                        temp = temp.next
                else:
                    temp.val = l1.val
                    temp.next = l1.next
                    break
            elif l2:
                    temp.val = l2.val
                    temp.next = l2.next
                    break
            else:
                break
        return nodeStart            
                    


# @lc code=end

