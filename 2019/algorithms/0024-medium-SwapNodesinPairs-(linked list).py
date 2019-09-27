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

# my solution
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        # setup
        dummy = ListNode(-1)
        dummy.next = head
        node_prev = dummy
        node_curr = head
        
        while node_curr is not None and node_curr.next is not None:
            # use [dummy, 1, 2, 3] as example in comment
            # (1) save node_curr.next as tmp node (node 2)
            node_curr_next = node_curr.next
            # (2) connect 1 to 3
            node_curr.next = node_curr.next.next
            # (3) connect 2 to 1
            node_curr_next.next = node_curr
            # (4) connect dummy to 2
            node_prev.next = node_curr_next
            # (5) update node_prev and node_curr, node_prev = node 1, node_curr = node 3
            node_prev = node_curr
            node_curr = node_curr.next
        
        return dummy.next