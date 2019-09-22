# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# iterative
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return None
        
        dummy = ListNode(0) # initialized as dummy node
        dummy.next = head
        node_prev = dummy
        node_curr = head
        
        while node_curr is not None:
            if node_curr.val == val:
                node_prev.next = node_curr.next
            else:
                node_prev = node_prev.next
            node_curr = node_curr.next
        
        return dummy.next
		
# with some redundant code
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return None
        
        dummy = ListNode(0) # initialized as dummy node
        dummy.next = head
        node_prev = dummy
        node_curr = head
        
        while node_curr is not None:
            if node_curr.val == val:
                node_prev.next = node_curr.next
                node_curr.next = None
                node_curr = node_prev.next
            else:
                node_curr = node_curr.next
                node_prev = node_prev.next
        
        return dummy.next