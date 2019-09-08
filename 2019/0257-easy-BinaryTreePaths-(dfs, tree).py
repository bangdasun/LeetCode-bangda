# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# iteration
class Solution:
    def getPath(self, root, path, output):
        # reach the leaf node, join all nodes in current path
        if root.left is None and root.right is None:
            output.append('->'.join(path))
            return
        
        # traverse left
        if root.left is not None:
            path.append(str(root.left.val))
            self.getPath(root.left, path, output)
            # backtracking
            path.pop()
        
        # backtracking traverse right
        if root.right is not None:
            path.append(str(root.right.val))
            self.getPath(root.right, path, output)
            # backtracking
            path.pop()
    
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root is None:
            return []
        
        output = []
        path = [str(root.val)]
        self.getPath(root, path, output)
        return output
		
# recursion
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root is None:
            return []
        
        if root.left is None and root.right is None:
            return [str(root.val)]
        
        output = []
        for path in self.binaryTreePaths(root.left):
            output.append(str(root.val) + '->' + path)
        
        for path in self.binaryTreePaths(root.right):
            output.append(str(root.val) + '->' + path)
        
        return output