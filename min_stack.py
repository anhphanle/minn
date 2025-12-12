class MinStack:
    def __init__(self):
        """
        PROBLEM: Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
        METHOD: O(1) Time for all ops. Two Stacks. 
        1. `stack`: Stores the actual values.
        2. `minStack`: Stores the minimum value encountered *so far* at each step.
        """
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # The new min is the smaller of 'val' or the current min (top of minStack)
        if not self.minStack:
            val = val
        else:
            val = min(val, self.minStack[-1])
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# --- Main Execution ---
if __name__ == "__main__":
    # Initialize the MinStack
    min_stack = MinStack()
    
    # Test Case: Push -2, 0, -3
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    
    # Check Min (Expected: -3)
    print(f"Current Min: {min_stack.getMin()}") 
    
    # Pop the top (-3 removed)
    min_stack.pop()
    
    # Check Top (Expected: 0)
    print(f"Top element: {min_stack.top()}") 
    
    # Check Min again (Expected: -2 because -3 is gone)
    print(f"Current Min: {min_stack.getMin()}")