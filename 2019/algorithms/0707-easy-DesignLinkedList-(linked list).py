class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index > self.size - 1 or index < 0:
            return -1
        
        count = 0
        node_curr = self.head
        while count < index:
            count += 1
            node_curr = node_curr.next
        return node_curr.val
        
    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. 
		After the insertion, the new node will be the first node of the linked list.
        """
        node = ListNode(val)
        if self.head is not None:
            node.next = self.head
        self.head = node
        self.size += 1
        return None

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = ListNode(val)
        if self.head is None:
            self.head = node
        
        node_curr = self.head
        while node_curr.next is not None:
            node_curr = node_curr.next
        node_curr.next = node
        self.size += 1
        return None

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. 
		If index equals to the length of linked list, the node will be appended to the end of linked list. 
		If index is greater than the length, the node will not be inserted.
        """
        if index <= 0:
            self.addAtHead(val)
            return None
        if index == self.size:
            self.addAtTail(val)
            return None
        if index > self.size - 1:
            return None
        count = 0
        node = ListNode(val)
        node_curr = self.head
        while count < index - 1:
            node_curr = node_curr.next
            count += 1
            
        if node_curr.next is not None:
            node_next = node_curr.next
            node_curr.next = node
            node.next = node_next
        self.size += 1
        return None

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index > self.size - 1 or index < 0:
            return None
        if index == 0:
            head_next = self.head.next
            self.head = head_next
            return None
        count = 0
        node_curr = self.head
        while count < index - 1:
            node_curr = node_curr.next
            count += 1
            
        if node_curr.next is not None:
            node_next = node_curr.next.next
            node_curr.next.next = None
            node_curr.next = node_next
        self.size -= 1
        return None

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)