# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def calcTreeSum(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        tree_sum = 0
        queue = []
        queue.append(root)
        
        while len(queue) > 0:
            for i in range(len(queue)):
                node = queue.pop(0)
                if node is not None:
                    tree_sum += node.val
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                    
        return tree_sum
        
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if root is None:
            return None
        
        subtree_sum_count = {}
        max_count = 1
        queue = []
        queue.append(root)
        
        while len(queue) > 0:
            for i in range(len(queue)):
                node = queue.pop(0)
                if node is not None:
                    subtree_sum = self.calcTreeSum(node)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                if subtree_sum not in subtree_sum_count:
                    subtree_sum_count[subtree_sum] = 1
                else:
                    subtree_sum_count[subtree_sum] += 1
                    
                max_count = max(subtree_sum_count[subtree_sum], max_count)
        
        output = []
        for subtree_sum, count in subtree_sum_count.items():
            if count == max_count:
                output.append(subtree_sum)
        
        return output
		
		
class Solution:
    def calcTreeSum(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        if root.left is None and root.right is None:
            return root.val
        
        return self.calcTreeSum(root.left) + self.calcTreeSum(root.right) + root.val 
        
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if root is None:
            return None
        
        subtree_sum_count = {}
        max_count = 1
        queue = []
        queue.append(root)
        
        while len(queue) > 0:
            for i in range(len(queue)):
                node = queue.pop(0)
                if node is not None:
                    subtree_sum = self.calcTreeSum(node)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                if subtree_sum not in subtree_sum_count:
                    subtree_sum_count[subtree_sum] = 1
                else:
                    subtree_sum_count[subtree_sum] += 1
                    
                max_count = max(subtree_sum_count[subtree_sum], max_count)
        
        output = []
        print(subtree_sum_count)
        for subtree_sum, count in subtree_sum_count.items():
            if count == max_count:
                output.append(subtree_sum)
        
        return output
