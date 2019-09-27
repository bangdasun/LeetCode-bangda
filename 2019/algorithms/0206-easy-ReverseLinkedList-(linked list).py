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
        
        # 1. create new_head
        new_head = None
        while head is not None:
            # 2. save head.next as tmp node
            head_next = head.next
            # 3. connect head to new_head (reverse)
            head.next = new_head
            # 4. update
            new_head = head
            head = head_next
        
        return new_head
