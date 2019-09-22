# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        dummy = TreeNode(0)
        dummy.right = root
        self.stack = [dummy]
        self.next()

    def next(self) -> int:
        """
        @return the next smallest number
        """
		# inorder traversal
        node = self.stack.pop()
        node_next = node
        if node.right is not None:
            node = node.right
            while node is not None:
                self.stack.append(node)
                node = node.left
        return node_next.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
