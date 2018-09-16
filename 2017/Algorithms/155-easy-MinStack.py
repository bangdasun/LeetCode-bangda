"""
https://leetcode.com/problems/min-stack/description/

"""

class MinStack:
    """
    Use two stacks
    First stack is normal stack, second stack is for storing minima of the first normal stack.
    (actually the top of the min stack is the minima)
    
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.normal = []
        self.min = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.normal.append(x)
        
        # if no value in min stack, just push the value into it;
        # or the value is smaller than current min, update min stack
        if len(self.min) == 0 or x <= self.getMin():
            self.min.append(x)

    def pop(self):
        """
        :rtype: void
        """
        # if the top of the normal stack is min, we need to update min stack 
        # (if we pop the current min from normal stack, we also need to pop it from min stack)
        # and always pop the normal stack
        if self.top() == self.getMin():
            self.min.pop(-1)
            
        self.normal.pop(-1)
        

    def top(self):
        """
        :rtype: int
        """
        return self.normal[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]
        


min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)
min_stack.getMin()
min_stack.pop()
min_stack.top()
min_stack.getMin()