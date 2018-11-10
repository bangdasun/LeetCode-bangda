# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        
        new_head = None
        curr = head.next
        head.next = None
        while curr is not None:
            # save the curr next 
            new_head = curr.next
            
            # change direction
            curr.next = head
            
            # update / move to next
            head = curr
            curr = new_head
        
        return head

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p