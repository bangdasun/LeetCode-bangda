# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        
        slow = head
        fast = head
        
        while fast is not None:
            # check if j.next exists
            if fast.next is None:
                break
				
            if fast.next is not None and fast.next == slow:
                return True
				
            slow = slow.next
            fast = fast.next.next
            
        return False