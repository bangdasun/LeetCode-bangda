
## Breadth First Search Summary

### 1. When to Use BFS

- Graph traversal (tree is also graph)
  - level order traversal
  - connected component
  - topological sorting
- Shortest path in simple graph (equal weights edges)

### 2. BFS in Tree

Three steps (same for all other structures like graph and matrix):

1. put all starting points into queue,
2. while queue is not empty:
3. for current level, extend all points in next level.

#### 2.1 Example: #102 - Binary Tree Level Order Traversal

```python
from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        
        # put all starting points into queue
        queue = deque([root])
        output = []
        while len(queue) > 0:
            level_output = []
            # level order traversal - need a for loop
            for _ in range(len(queue)):
                # current level - add to output
                node = queue.popleft()
                level_output.append(node.val)
                # extend to next level - add to queue
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            # add current level to output
            output.append(level_output)
        
        return output
```

If it is no need to do level order traversal, the `for` loop can be **removed**.

Other Examples with Same Traverse Steps:

- #101 - Symmetric Tree
- #103 - Binary tree Zigzag Level Order Traversal
- #107 - Binary Tree Level Order Traversal II
- #111 - Minimum Depth of Binary Tree
- #116 - Populating Next Right Pointers in Each Node
- #199 - Binary Tree Right Side View
- #297 - Serialize and Deserialize Binary Tree
- #429 - N-arg Tree Level Order Traversal
- #513 - Find Bottom Left Tree Value
- #515 - Find Largest Value in Each Tree Row
- #559 - Maximum Depth of N-ary Tree
- #993 - Cousins in Binary Tree
- lintcode #242 - Convert Binary Tree to Linked Lists by Depth

Here:

-  #101 and #993 require some tricky array operations during the level order traversal, needs to be careful.
- #116 and lintcode #242 require linked list nodes operations.

### 3. BFS in Graph

Difference with tree: graph can have cycles / rings. When implement BFS on graph, it will needs a `visited` hashset to store visited nodes to make sure no duplicate visit / revisit happens.

#### 3.1 Example: #133 - Clone Graph

So compared with BFS in tree, here we need a `visited` set to store visited nodes. Clone, i.e. deep copy, is implemented by using a mapping dictionary maps from old nodes to new nodes.

```python
from collections import deque

class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

class Solution:
    def getNodes(self, node: 'Node'):
        queue = deque([node])
        visited = set([node])
        while len(queue) > 0:
            curr_node = queue.popleft()
            for neighbor in curr_node.neighbors:
                if neighbor in visited:
                    continue
                queue.append(neighbor)
                visited.add(neighbor)
                
        return list(visited)
        
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        
        # G = (E, V)
        # 1. copy nodes
        # 2. copy edges
        root = node
        all_nodes = self.getNodes(root)
        
        # create a mapping from old nodes to new nodes
        old_to_new = {}
        
        # copy nodes
        for node in all_nodes:
            old_to_new[node] = Node(val=node.val, neighbors=[])
        
        # copy edges
        for node in all_nodes:
            new_node = old_to_new[node]
            for neighbor in node.neighbors:
                new_neighbor = old_to_new[neighbor]
                new_node.neighbors.append(new_neighbor)
        
        return old_to_new[root]
```

#### 3.2 Example: #127 - Word Ladder

This is a **implicit graph** case.

```python
from collections import deque

class Solution:
    def countCommonLetters(self, wordA, wordB):
        n = len(wordA)
        count = 0
        for i in range(n):
            if wordA[i] == wordB[i]:
                count += 1
        return count
        
    def getNextWords(self, beginWord, wordList, visited):
        next_words = []
        n = len(beginWord)
        for w in wordList:
            if w in visited:
                continue
            if self.countCommonLetters(beginWord, w) != n - 1:
                continue
            next_words.append(w)
        return next_words
        
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = deque([beginWord])
        visited = set([beginWord])
        distance = 1
        
        while len(queue) > 0:
            # level order traversal
            for _ in range(len(queue)):
                word = queue.popleft()
                for next_word in self.getNextWords(word, wordList, visited):
                    if next_word == endWord:
                        return distance + 1
                    queue.append(next_word)
                    visited.add(next_word)
            distance += 1
            
        return 0
```

### 4. BFS in Matrix

Matrix is also a graph.

#### 4.1 Example #200 - Number of Islands

Do BFS for unseen island, the BFS will traverse current island. The number of running BFS is the number of island.

```python
from collections import deque

class Solution:
    def is_unknow_island(self, grid, x, y, visited):
        nrow = len(grid)
        ncol = len(grid[0])
        return 0 <= x < nrow and \
               0 <= y < ncol and \
               (x, y) not in visited and \
               grid[x][y] == '1'
    
    def bfs(self, grid, x, y, visited):
        queue = deque([(x, y)])
        visited.add((x, y))
        while len(queue) > 0:
            x, y = queue.popleft()
            for delta_x, delta_y in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                next_x = x + delta_x
                next_y = y + delta_y
                if not self.is_unknow_island(grid, next_x, next_y, visited):
                    continue
                queue.append((next_x, next_y))
                visited.add((next_x, next_y))
                
        return visited
        
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid is None:
            return 0
        
        nrow = len(grid)
        if nrow == 0:
            return 0
        
        ncol = len(grid[0])
        visited = set()
        num_islands = 0
        
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == '1' and (i, j) not in visited:
                    visited = self.bfs(grid, i, j, visited)
                    num_islands += 1
        
        return num_islands
```

Other examples:

- #130 - Surrounded Regions

#### 4.2 Example #542 - 01 Matrix

This is about **shortest path** in matrix. For each 1, search for nearest 0 using BFS with level order traversal, the number of levels used is the distance to nearest 0.

```python
from collections import deque

class Solution:
    def is_valid(self, matrix: List[List[int]], x: int, y: int):
        nrow = len(matrix)
        if nrow == 0:
            return False
        
        ncol = len(matrix[0])
        return 0 <= x < nrow and 0 <= y < ncol
    
    def bfs(self, matrix: List[List[int]], x: int, y: int, distance: List[List[int]]):
        queue = deque([(x, y)])
        visited = set((x, y))
        while len(queue) > 0:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for delta_i, delta_j in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                    next_i = i + delta_i
                    next_j = j + delta_j
                    if not self.is_valid(matrix, next_i, next_j):
                        continue
                    if (next_i, next_j) in visited:
                        continue
                    if matrix[next_i][next_j] == 0:
                        return distance
                    queue.append((next_i, next_j))
                    visited.add((next_i, next_j))
            distance[x][y] += 1
            
        return distance
                    
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if matrix is None:
            return matrix
        
        nrow = len(matrix)
        if nrow == 0:
            return matrix
        
        ncol = len(matrix[0])
        distance = [[0 for j in range(ncol)] for i in range(nrow)]
        
        for i in range(nrow):
            for j in range(ncol):
                if matrix[i][j] == 1:
                    distance[i][j] += 1
                    distance = self.bfs(matrix, i, j, distance)
        
        return distance
```

Other examples about shortest path in matrix:
- #934 - Shortest Bridge
- #994 - Rotting Oranges
- #1091 - Shortest Path Binary Matrix
- #1162 - As Far from Land as Possible
- lintcode #611 - Knight Shortest Path

In general, there are following steps:

1. get all starting points and put them into queue
2. while queue is not empty:
3. each loop do level order traversal, save number of times running search
4. need some help functions to determine whether search is in bounds / whether the input is in edge cases

### 5. Topological Sorting

Has to be on **directed graph**. 

General steps:

1. get the indegree of every node
2. put all nodes with zero indegree into the queue as start
3. keep popping nodes from queue, remove its connections to other points, reduce the indegree of other nodes by 1
4. append nodes with zero indegree to queue

The results are not unique, it is also possible to have no results (no nodes have zero indegree, after the while loop, check if the total number of nodes is equal to the length of the output nodes).

Four basic question format:

1. find a topological order
2. whether exists a topological order (whether total number of nodes equals number of output nodes)
3. find all topological orders (use DFS)
4. whether topological order is unique (the queue must have only one node every time)

#### 5.1 Example - Lintcode #127 Topological Sorting

```python
from collections import deque

class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def get_indegree(self, graph):
        node_to_indegree = {x: 0 for x in graph}
        
        for node in graph:
            for neighbor in node.neighbors:
                node_to_indegree[neighbor] += 1
                
        return node_to_indegree
        
    def topSort(self, graph):
        if graph is None:
            return None
        
        node_to_indegree = self.get_indegree(graph)
        queue = deque([node for node in node_to_indegree \
                       if node_to_indegree[node] == 0])
        output = []
        while len(queue) > 0:
            node = queue.popleft()
            output.append(node)
            for neighbor in node.neighbors:
                node_to_indegree[neighbor] -= 1
                if node_to_indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return output
```

Other examples:

- #207 - Course Schedule
- #210 - Course Schedule II
- #444 - (lintcode #605) Sequence Reconstruction

The steps for sorting is simple, the key part is how to construct the graph to run the sort.

### 6. BFS Time Complexity

In general time complexity for BFS in a graph is `O(m+n)` where `m` is the number of edges and `n` is the number of vertex. In binary tree the time complexity is `O(n)` where `n` is the number of tree nodes.

#### X. Tips and Notice

- Queue structure is used for BFS, queue is "first in first out".
- In python, queue structure is `collections.deque`, dequeue method is `.popleft()`. Python `list` is **stack**, therefore `.pop(0)` is `O(n)`.
