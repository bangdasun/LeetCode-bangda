# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# recursive
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        next_new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return next_new_head
        
# iterative
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        new_head = None
        while head is not None:
            # save head.next
            head_next = head.next
            
            # update
            # 1. connect
            head.next = new_head
            # 2. move
            new_head = head
            head = head_next
        
        return new_head
