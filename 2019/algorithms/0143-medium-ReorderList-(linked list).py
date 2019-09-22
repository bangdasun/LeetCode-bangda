# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        new_head = None
        while head is not None:
            head_next = head.next
            head.next = new_head
            new_head = head
            head = head_next
        return new_head
        
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return None
        
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        second_half_head = self.reverseList(slow)
        first_half_node = head
        
        # first and second half have same node, second half should stop before it
		# second half will be longer than first half by 1 if length is odd number
        while second_half_head.next is not None and first_half_node is not None:
            first_half_node_next = first_half_node.next
            second_half_head_next = second_half_head.next
            
            first_half_node.next = second_half_head
            second_half_head.next = first_half_node_next
            
            first_half_node = first_half_node_next
            second_half_head = second_half_head_next
        
        return None
