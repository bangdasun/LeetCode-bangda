# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# refer from https://www.cnblogs.com/grandyang/p/4441680.html
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        node_prev = dummy
        
        while node_prev.next is not None and node_prev.next.next is not None:
            # 5 steps
            # 1. next prev
            node_next = node_prev.next.next
            # 2. 
            node_prev.next.next = node_next.next
            # 3. swap
            node_next.next = node_prev.next
            # 4.
            node_prev.next = node_next
            # 5. update node_prev
            node_prev = node_next.next
        
        return dummy.next
