from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        PROBLEM: Return an array where answer[i] is the number of days to wait for a warmer temperature.
        METHOD: O(n) Time, O(n) Space. Monotonic Decreasing Stack. 
        Store indices in stack. If current temp > temp at stack top, we found the warmer day -> pop and record difference.
        """
        res = [0] * len(temperatures)
        stack = []  # Stores indices of days

        for i, t in enumerate(temperatures):
            # Check if current day is warmer than the day at the top of the stack
            while stack and t > temperatures[stack[-1]]:
                stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append(i)
            
        return res

# --- Main Execution ---
if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: Standard case
    temps1 = [73, 74, 75, 71, 69, 72, 76, 73]
    print(f"Test 1: {sol.dailyTemperatures(temps1)}") 
    # Expected: [1, 1, 4, 2, 1, 1, 0, 0]

    # Test Case 2: Monotonically increasing
    temps2 = [30, 40, 50, 60]
    print(f"Test 2: {sol.dailyTemperatures(temps2)}") 
    # Expected: [1, 1, 1, 0]

    # Test Case 3: Monotonically decreasing
    temps3 = [30, 60, 90]
    print(f"Test 3: {sol.dailyTemperatures(temps3)}") 
    # Expected: [1, 1, 0]