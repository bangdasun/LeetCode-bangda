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
        # merged list: head is None
		merged = ListNode(None)
		
		# tail Node
        temp = ListNode(None)
        merged = temp
            
        if l1 is not None and l2 is not None:
            while l1 is not None and l2 is not None:
                if l1.val <= l2.val:
                    temp.next = ListNode(l1.val)
                    l1 = l1.next    
                else:
                    temp.next = ListNode(l2.val)
                    l2 = l2.next
                temp = temp.next
            # l1 is empty and l2 not
            if l2 is not None:
                temp.next = l2
                temp = temp.next
            # l2 is empty and l1 not
            if l1 is not None:
                temp.next = l1
                temp = temp.next
        
        elif l1 is None:
            merged.next = l2
            
        elif l2 is None:
            merged.next = l1
            
        return merged.next
		
# Recursion 
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
        
        if l1.val <= l2.val:
            merged = l1
            merged.next = self.mergeTwoLists(l1.next, l2)
        else:
            merged = l2
            merged.next = self.mergeTwoLists(l1, l2.next)
            
        return merged