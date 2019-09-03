# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ''
        
        queue = deque([root])
        output = []
        
        while len(queue) > 0:
            for _ in range(len(queue)):
                node = queue.popleft()
                output.append(str(node.val) if node is not None else '#')
                if node is not None:
                    queue.append(node.left)
                    queue.append(node.right)
        
        return ' '.join(output)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data is None or len(data) == 0:
            return None
            
        bfs_order = [TreeNode(int(val)) if val != '#' else None for val in data.split()]
        
        root = bfs_order[0]
        nodes = [root]
        slow_index, fast_index = 0, 1
        
        while slow_index < len(nodes):
            node = nodes[slow_index]
            slow_index += 1
            node.left = bfs_order[fast_index]
            node.right = bfs_order[fast_index + 1]
            fast_index += 2
            
            if node.left is not None:
                nodes.append(node.left)
            if node.right is not None:
                nodes.append(node.right)
        
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
