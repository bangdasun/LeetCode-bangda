# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# refer from https://www.cnblogs.com/grandyang/p/5138936.html
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        node_prev = head
        node_curr = head.next
        
        while node_curr is not None and node_curr.next is not None:
            # 5 steps
            # 1. create tmp
            tmp = node_prev.next
            # 2. 
            node_prev.next = node_curr.next
            # 3. 
            node_curr.next = node_curr.next.next
            # 4.
            node_prev.next.next = tmp
            # 5. update
            node_prev = node_prev.next
            node_curr = node_curr.next
        
        return head

# my solution
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        # setup
        node_prev = head
        node_curr = head.next
        
        while node_curr is not None and node_curr.next is not None:
            # use [1, 2, 3, 4] as example in comment
            # (1) save node_prev.next as tmp node (node 2)
            #     since node_curr will be update soon
            node_prev_next = node_prev.next
            # (2) connect 1 to 3
            node_prev.next = node_curr.next
            # (3) connect 3 to 2
            node_curr.next = node_curr.next.next
            # (4) connect 2 to 4
            node_prev.next.next = node_prev_next
            # (5) update node_prev = node 3, node_curr = node 4
            node_prev = node_prev.next
            node_curr = node_curr.next
        
        return head
