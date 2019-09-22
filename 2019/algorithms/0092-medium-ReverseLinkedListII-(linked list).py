# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode, length: int) -> ListNode:
        if head is None or head.next is None:
            return head
        
        new_head = None
        index = 0
        while index <= length:
            head_next = head.next
            head.next = new_head
            new_head = head
            head = head_next
            index += 1
            
        return new_head
        
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if head is None or head.next is None:
            return head
        
        index = 1
        dummy = ListNode(-1)
        dummy.next = head
        node_prev = dummy
        node_curr = head
        node_start = None
        node_end_next = None
        
        # get the start and end nodes of reversed part
        while index <= n:
            if index <= m:
                node_start = node_curr
                node_start_prev = node_prev
            node_prev = node_prev.next
            node_curr = node_curr.next
            index += 1
        
        # first node after reversed part
        node_end_next = node_curr
        
        # reverse
        new_node_curr = self.reverseList(node_start, n - m)
        
        # connect first part and reversed part
        node_start_prev.next = new_node_curr
        
        # get to the end of reversed part
        while new_node_curr.next is not None:
            new_node_curr = new_node_curr.next
            
        # connect reversed part and second part
        new_node_curr.next = node_end_next
        
        return dummy.next
