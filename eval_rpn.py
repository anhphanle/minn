from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        PROBLEM: Evaluate the value of an arithmetic expression in Reverse Polish Notation.
        METHOD: O(n) Time, O(n) Space. Stack. Iterate tokens. If number, push to stack. If operator, pop top two elements, apply operation, and push result back. Note: Division truncates toward zero.
        """
        stack = []
        
        for t in tokens:
            if t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            elif t == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif t == "/":
                a, b = stack.pop(), stack.pop()
                # Use int() conversion to truncate towards zero (Python's // is floor division)
                stack.append(int(b / a))
            else:
                stack.append(int(t))
                
        return stack[0]

# --- Main Execution ---
if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: (2 + 1) * 3
    tokens1 = ["2","1","+","3","*"]
    print(f"Test 1: {sol.evalRPN(tokens1)}") # Expected: 9
    
    # Test Case 2: 4 + (13 / 5) -> 4 + 2 = 6
    tokens2 = ["4","13","5","/","+"]
    print(f"Test 2: {sol.evalRPN(tokens2)}") # Expected: 6

    # Test Case 3: Complex with negatives
    tokens3 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(f"Test 3: {sol.evalRPN(tokens3)}") # Expected: 22