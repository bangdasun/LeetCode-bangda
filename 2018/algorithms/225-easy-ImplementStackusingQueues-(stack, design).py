class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q2 = []
        self.q1 = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        if len(self.q1) > 0:
            self.q2.append(x)
            while len(self.q1) > 0:
                self.q2.append(self.q1.pop(0))
        elif len(self.q2) > 0:
            self.q1.append(x)
            while len(self.q2) > 0:
                self.q1.append(self.q2.pop(0))
        else:
            self.q1.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if len(self.q1) == 0:
            return self.q2.pop(0)
        elif len(self.q2) == 0:
            return self.q1.pop(0)
            
    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if len(self.q1) == 0:
            return self.q2[0]
        elif len(self.q2) == 0:
            return self.q1[0]
        
    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.q1) == 0 and len(self.q2) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()