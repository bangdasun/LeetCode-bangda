# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # define a queue for BFS
        queue = []
        queue.append(root)
        queue.append(root)
        
        while len(queue) > 0:
            node_left = queue.pop(0)
            node_right = queue.pop(0)
            if node_left is None and node_right is None:
                continue
            if node_left is None or node_right is None:
                return False
            if node_left.val != node_right.val:
                return False
            queue.append(node_left.left)
            queue.append(node_right.right)
            queue.append(node_left.right)
            queue.append(node_right.left)
        
        return True

# use level order traversal
from collections import deque

class Solution:
    def isSymmetricArr(self, arr) -> bool:
        if arr is None:
            return True
        
        n = len(arr)
        if n > 1 and n % 2 == 1:
            return False
        
        left, right = 0, n - 1
        while left < right:
            if arr[left] != arr[right]:
                return False
            left += 1
            right -= 1
        return True
    
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        
        queue = deque([root])
        while len(queue) > 0:
            level_output = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node is None:
                    level_output.append('null')
                else:
                    level_output.append(str(node.val))
                    queue.append(node.left)
                    queue.append(node.right)
            level_result = self.isSymmetricArr(level_output)
            if not level_result:
                return False
        
        return True
