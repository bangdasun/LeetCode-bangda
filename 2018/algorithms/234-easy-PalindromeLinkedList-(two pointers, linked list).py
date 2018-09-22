# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    
    def reverse(self, node):
        if node is None or node.next is None:
            return node
        
        head = None
        
        # save the next
        curr = node.next
        
        # change the direction
        node.next = None
        while curr is not None:
            # save the next node
            head = curr.next
            
            # change the new head direction
            curr.next = node
            
            # move to next node
            node = curr
			curr = head
            
        return node
                
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True
        
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        # now the slow is at the middle, since fast is twice faster as slow
        # and then reverse: direction change
        curr = self.reverse(slow)
        while curr is not None:
            print(curr.val, head.val)
            
            if curr.val != head.val:
                return False
            # from right to left
            curr = curr.next
            
            # from left to right
            head = head.next
        
        return True
        