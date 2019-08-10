class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue_1 = []
        self.queue_2 = []
        
    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue_1.append(x)
        
    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if not self.empty():
            queue_1_size = len(self.queue_1)
            for i in range(queue_1_size - 1):
                x = self.queue_1.pop(0)
                self.queue_2.append(x)
                
            output = self.queue_1.pop(0)
            
            queue_2_size = len(self.queue_2)
            for i in range(queue_2_size):
                x = self.queue_2.pop(0)
                self.queue_1.append(x)
            return output
                
    def top(self) -> int:
        """
        Get the top element.
        """
        if not self.empty():
            return self.queue_1[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue_1) == 0 and len(self.queue_2) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()