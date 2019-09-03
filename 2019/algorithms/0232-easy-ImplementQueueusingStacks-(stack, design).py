class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_1 = []
        self.stack_2 = []
        
    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack_1.append(x)
        
    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.empty():
            stack_1_size = len(self.stack_1)
            for i in range(stack_1_size):
                x = self.stack_1.pop()
                self.stack_2.append(x)
            
            output = self.stack_2.pop()
            stack_2_size = len(self.stack_2)
            for i in range(stack_2_size):
                x = self.stack_2.pop()
                self.stack_1.append(x)
            
            return output

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.empty():
            return self.stack_1[0]
        
    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack_1) == 0 and len(self.stack_2) == 0
        

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()