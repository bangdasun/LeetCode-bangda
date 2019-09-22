# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        
        if l2 is None:
            return l1
        
        l1_curr = l1
        l2_curr = l2
        
        # dummy head
        merged = ListNode(0)
        curr = merged
        
        while l1_curr is not None and l2_curr is not None:
            if l1_curr.val < l2_curr.val:
                curr.next = l1_curr
                l1_curr = l1_curr.next
            else:
                curr.next = l2_curr
                l2_curr = l2_curr.next
            curr = curr.next
        
        if l1_curr is not None:
            curr.next = l1_curr
        if l2_curr is not None:
            curr.next = l2_curr
            
        return merged.next
