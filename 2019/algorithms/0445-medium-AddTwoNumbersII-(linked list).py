# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getNumber(self, head):
        if head is None:
            return 0
        
        digit_count = 0
        number = 0
        head_curr = head
        while head_curr is not None:
            head_curr = head_curr.next
            digit_count += 1
        
        while head is not None:
            number += head.val * 10 ** (digit_count - 1)
            digit_count -= 1
            head = head.next
        
        return number
            
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        
        if l2 is None:
            return l1
        
        l1_number = self.getNumber(l1)
        l2_number = self.getNumber(l2)
        sum = str(l1_number + l2_number)
        dummy = ListNode(-1)
        node_curr = dummy
        for i in sum:
            node_curr.next = ListNode(int(i))
            node_curr = node_curr.next
        
        return dummy.next
