
## Linked List Summary

### 1. Linked List Iteration

In generate, use `.next` to iterate through the linked list, remember to make sure `.next` can only applied on non empty list node.

#### 1.2 Example #876 - Middle of the Linked List

Use two pointers - `fast` and `slow`, `fast` moves twice faster than `slow`.

```python
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        
        slow = head
        fast = head
        
        # condition: fast and fast.next 
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        return slow
```

Another example need to use the middle of the linked list:

- #141 - Linked List Cycle
- #234 - Palindrome Linked List

### 2. Linked List Reorganization

#### 2.1 Remove Nodes From Linked List

Need a `dummy` head before head, since `head` might be changed.

##### 2.1.1 Example #19 - Remove Nth Node From End of List

```python
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head is None:
            return None
        
        node_curr = head
        list_len = 0
        while node_curr is not None:
            node_curr = node_curr.next
            list_len += 1
        
        # setup
        remove_index = list_len - n
        index = 0
        dummy = ListNode(-1)
        dummy.next = head
        node_prev = dummy
        node_curr = head
        
        while index < remove_index:
            node_prev = node_prev.next
            node_curr = node_curr.next
            index += 1
        
        # remove node - skip current node
        node_prev.next = node_curr.next
        node_curr.next = None
        
        return dummy.next
```

Other examples:

- #82 - Remove Duplicates from Sorted List II
- #83 - Remove Duplicates from Sorted List

#### 2.2 Reverse Linked List

#### 2.2.1 Example #206 - Reverse Linked List

Four steps:

1. create a `new_head` node first
2. save `head.next` as a tmp node
3. let `head` connects to `new_head`
4. update `new_head` and `head` (update needs to be from left to right).

```python
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        # 1. create new_head
        new_head = None
        while head is not None:
            # 2. save head.next as tmp node
            head_next = head.next
            # 3. connect head to new_head (reverse)
            head.next = new_head
            # 4. update
            new_head = head
            head = head_next
        
        return new_head
```

Other examples:

- #92 - Reverse Linked List II
- #234 - Palindrome Linked List

#### 2.3 Other Reorganization

##### 2.3.1 Example #24 - Swap Nodes in Pairs

```python
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        # setup
        dummy = ListNode(-1)
        dummy.next = head
        node_prev = dummy
        node_curr = head
        
        while node_curr is not None and node_curr.next is not None:
            # use [dummy, 1, 2, 3] as example in comment
            # (1) save node_curr.next as tmp node (node 2)
            node_curr_next = node_curr.next
            # (2) connect 1 to 3
            node_curr.next = node_curr.next.next
            # (3) connect 2 to 1
            node_curr_next.next = node_curr
            # (4) connect dummy to 2
            node_prev.next = node_curr_next
            # (5) update node_prev = node 1, node_curr = node 3
            node_prev = node_curr
            node_curr = node_curr.next
        
        return dummy.next
```

##### 2.3.2 Example #328 - Odd Even Linked List #

```python
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        # setup
        node_prev = head
        node_curr = head.next
        
        while node_curr is not None and node_curr.next is not None:
            # use [1, 2, 3, 4] as example in comment
            # (1) save node_prev.next as tmp node (node 2)
            #     since node_curr will be update soon
            node_prev_next = node_prev.next
            # (2) connect 1 to 3
            node_prev.next = node_curr.next
            # (3) connect 3 to 2
            node_curr.next = node_curr.next.next
            # (4) connect 2 to 4
            node_prev.next.next = node_prev_next
            # (5) update node_prev = node 3, node_curr = node 4
            node_prev = node_prev.next
            node_curr = node_curr.next
        
        return head
```

##### 2.3.3 Example #143 Reorder List

```python
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        new_head = None
        while head is not None:
            head_next = head.next
            head.next = new_head
            new_head = head
            head = head_next
        return new_head
        
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return None
        
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        second_half_head = self.reverseList(slow)
        first_half_node = head
        
        # first and second half have same node, second half should stop before it
        while second_half_head.next is not None and first_half_node is not None:
            # (1) save next nodes as tmp nodes
            first_half_node_next = first_half_node.next
            second_half_head_next = second_half_head.next
            # (2) cross connect
            first_half_node.next = second_half_head
            second_half_head.next = first_half_node_next
            # (3) update
            first_half_node = first_half_node_next
            second_half_head = second_half_head_next
        
        return None
```

### 3. Generate New Linked List

Need a `dummy` head before `head`.

#### 3.1 Example lintcode #242 - Convert Binary Tree to Linked Lists by Depth

Here the only part related to linked list is creating a linked list from an array

```python
node_dummy = ListNode(0)
node_curr = node_dummy
for i in range(len(array)):
    node_curr.next = ListNode(array[i])
    node_curr = node_curr.next

head = node_dummy.next
```

#### 3.2 Example #21- Merge Two Sorted Lists

```python
class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        
        if l2 is None:
            return l1
        
        l1_curr = l1
        l2_curr = l2
        
        # dummy head
        merged = ListNode(-1)
        curr = merged
        
        while l1_curr is not None and l2_curr is not None:
            if l1_curr.val < l2_curr.val:
                curr.next = l1_curr
                l1_curr = l1_curr.next
            else:
                curr.next = l2_curr
                l2_curr = l2_curr.next
            curr = curr.next
        
        if l1_curr is not None:
            curr.next = l1_curr
        if l2_curr is not None:
            curr.next = l2_curr
            
        return merged.next
```

Other examples:

- #2 - Add Two Numbers
- #445 - Add Two Numbers II

#### X. Tips and Notice

