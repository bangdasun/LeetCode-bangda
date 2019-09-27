# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# use hashset
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        
        hashset = set()
        node_curr = head
        while node_curr is not None:
            if node_curr in hashset:
                return node_curr
            hashset.add(node_curr)
            node_curr = node_curr.next
        
        return None