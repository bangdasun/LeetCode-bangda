"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""

from collections import deque

class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        if root is None:
            return []
    
        queue = deque([root])
        output = []
        while len(queue) > 0:
            level_output = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level_output.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            
			# create linked list from array
            node_dummy = ListNode(0)
            node_dummy.next = None
            node_curr = node_dummy
            for i in range(len(level_output)):
                node_next = ListNode(level_output[i])
                node_curr.next = node_next
                node_curr = node_next
            output.append(node_dummy.next)
        return output
            