from typing import List

class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        """
        PROBLEM: Find indices of two numbers in `nums` that add up to `target`.
        METHOD: O(n) Hash Map. Iterate `nums`, check if `target - num` exists in `seen` map.
        """
        seen = {}  # val -> index

        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i
            
        return []

# --- Main Execution ---
if __name__ == "__main__":
    # Initialize the solution
    sol = Solution()
    
    # Test Case 1
    nums1, target1 = [2, 7, 11, 15], 9
    print(f"Test 1: {sol.two_sum(nums1, target1)}")  # Expected: [0, 1]

    # Test Case 2
    nums2, target2 = [3, 2, 4], 6
    print(f"Test 2: {sol.two_sum(nums2, target2)}")  # Expected: [1, 2]

    # Test Case 3
    nums3, target3 = [3, 3], 6
    print(f"Test 3: {sol.two_sum(nums3, target3)}")  # Expected: [0, 1]