class Solution:
    def isValid(self, s: str) -> bool:
        """
        PROBLEM: Determine if the input string has valid parentheses order (opened and closed correctly).
        METHOD: O(n) Time, O(n) Space. Stack (LIFO). 
        Iterate `s`. Push opening brackets to stack. For closing brackets, check if stack matches the top element via a Hash Map.
        """
        stack = []
        closeToOpen = {")": "(", "]": "[", "}": "{"}
        
        for char in s:
            if char in closeToOpen:
                # It is a closing bracket
                # Check if stack is not empty AND top matches
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False
            else:
                # It is an opening bracket
                stack.append(char)
                
        # True if stack is empty (all brackets matched)
        return True if not stack else False

# --- Main Execution ---
if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: Simple pair
    s1 = "()"
    print(f"Test 1 ('{s1}'): {sol.isValid(s1)}") # Expected: True
    
    # Test Case 2: Mixed valid pairs
    s2 = "()[]{}"
    print(f"Test 2 ('{s2}'): {sol.isValid(s2)}") # Expected: True

    # Test Case 3: Mismatch
    s3 = "(]"
    print(f"Test 3 ('{s3}'): {sol.isValid(s3)}") # Expected: False

    # Test Case 4: Nested but wrong order
    s4 = "([)]"
    print(f"Test 4 ('{s4}'): {sol.isValid(s4)}") # Expected: False