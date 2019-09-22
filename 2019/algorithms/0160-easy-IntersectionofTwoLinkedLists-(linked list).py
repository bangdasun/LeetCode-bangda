# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# use hashset
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        
        nodeA_curr = headA
        nodeA_set = set([nodeA_curr])
        while nodeA_curr is not None:
            nodeA_curr = nodeA_curr.next
            nodeA_set.add(nodeA_curr)
        
        nodeB_curr = headB
        while nodeB_curr is not None:
            if nodeB_curr in nodeA_set:
                return nodeB_curr
            nodeB_curr = nodeB_curr.next
            
        return None
