# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def processSum(self, sum_curr, add_one):
        if add_one:
            sum_curr += 1
        if sum_curr > 9:
            add_one = 1
            sum_curr = sum_curr % 10
        else:
            add_one = 0
        return sum_curr, add_one
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        
        if l2 is None:
            return l1
        
        add_one = 0
        dummy = ListNode(-1)
        node_curr = dummy
        
        while l1 is not None and l2 is not None:
            sum_curr = l1.val + l2.val
            sum_curr, add_one = self.processSum(sum_curr, add_one)
            node_curr.next = ListNode(sum_curr)
            node_curr = node_curr.next
            l1 = l1.next
            l2 = l2.next
        
        while l1 is not None:
            sum_curr = l1.val
            sum_curr, add_one = self.processSum(sum_curr, add_one)
            node_curr.next = ListNode(sum_curr)
            node_curr = node_curr.next
            l1 = l1.next
        
        while l2 is not None:
            sum_curr = l2.val
            sum_curr, add_one = self.processSum(sum_curr, add_one)
            node_curr.next = ListNode(sum_curr)
            node_curr = node_curr.next
            l2 = l2.next
                
        if add_one:
            node_curr.next = ListNode(1)
        
        return dummy.next
