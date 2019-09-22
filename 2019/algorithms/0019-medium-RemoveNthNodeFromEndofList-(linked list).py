# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head is None:
            return None
        
        node_curr = head
        list_len = 0
        while node_curr is not None:
            node_curr = node_curr.next
            list_len += 1
        
        remove_index = list_len - n
        index = 0
        dummy = ListNode(0)
        dummy.next = head
        node_prev = dummy
        node_curr = head
        
        while index < remove_index:
            node_prev = node_prev.next
            node_curr = node_curr.next
            index += 1
        
        node_prev.next = node_curr.next
        node_curr.next = None
        
        return dummy.next
