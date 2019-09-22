# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        dummy = ListNode(-1)
        dummy.next = head
        node_prev = dummy
        node_curr = head
        
        while node_curr is not None and node_curr.next is not None:
            if node_curr.val == node_curr.next.val:
                node_next = node_curr.next
                node_val = node_curr.val
                while node_curr is not None and node_curr.val == node_val:
                    node_curr = node_curr.next
                node_prev.next = node_curr
            else:
                node_prev = node_curr
                node_curr = node_curr.next
            
        return dummy.next
