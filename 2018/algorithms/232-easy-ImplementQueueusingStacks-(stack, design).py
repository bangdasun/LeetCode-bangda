class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        if len(self.s1) > 0:
            self.s1.append(x)
        elif len(self.s2) > 0:
            self.s2.append(x)
        else:
            self.s1.append(x)
        
    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.s1) > 0:
            while len(self.s1) > 1:
                self.s2.append(self.s1.pop())
            num = self.s1.pop()
            
            while len(self.s2) > 0:
                self.s1.append(self.s2.pop())
            
            return num
        elif len(self.s2) > 0:
            while len(self.s2) > 1:
                self.s1.append(self.s2.pop())
            num = self.s2.pop()
            
            while len(self.s1) > 0:
                self.s2.append(self.s1.pop())
            
            return num
            
    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.s1) > 0:
            return self.s1[0]
        elif len(self.s2) > 0:
            return self.s2[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.s1) == 0 and len(self.s2) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()