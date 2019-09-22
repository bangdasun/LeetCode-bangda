# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode):
        if root is None:
            return []
        
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if root is None:
            return False
        
        if root.left is None and root.right is None:
            return False
        
        arr = self.inorderTraversal(root)
        print(arr, k)
        n = len(arr)
        left, right = 0, n - 1
        while left < right:
            while left < right and arr[left] + arr[right] < k:
                left += 1
            while left < right and arr[left] + arr[right] > k:
                right -= 1
            while left < right and arr[left] + arr[right] == k:
                return True
        return False
