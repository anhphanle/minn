from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        PROBLEM: Detect if `nums` contains any duplicate values.
        METHOD: O(n) Hash Set. Iterate through `nums`, check if `num` is already in `seen` set.
        """
        seen = set()
        
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
            
        return False

# --- Main Execution ---
if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: Standard duplicates
    nums1 = [1, 2, 3, 1]
    print(f"Test 1 {nums1}: {sol.containsDuplicate(nums1)}") # Expected: True
    
    # Test Case 2: Distinct elements
    nums2 = [1, 2, 3, 4]
    print(f"Test 2 {nums2}: {sol.containsDuplicate(nums2)}") # Expected: False

    # Test Case 3: Multiple duplicates
    nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(f"Test 3 {nums3}: {sol.containsDuplicate(nums3)}") # Expected: True