# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head) -> ListNode:
        if head is None or head.next is None:
            return head
        
        new_head = None
        while head is not None:
            head_next = head.next
            head.next = new_head
            new_head = head
            head = head_next
        
        return new_head
        
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True
        
        slow = head
        fast = head
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        # slow is in middle, not slow.next
        second_half_head = self.reverseList(slow)
        while second_half_head is not None:
            if second_half_head.val != head.val:
                return False
				
            # from right to left
            second_half_head = second_half_head.next
            # from left to right
            head = head.next
        
        return True