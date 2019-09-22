# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        
        dummy = ListNode(-1) # return dummy.next will be an issue if head.val = -1
        dummy.next = head
        node_prev = dummy
        node_curr = head
        
        while node_prev is not None and node_curr is not None:
            if node_prev.val != node_curr.val:
                node_prev = node_prev.next
            else:
                node_prev.next = node_curr.next
            node_curr = node_curr.next
        
        # different from #203 since this is not delete node
        return head
