from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        PROBLEM: Find all unique triplets [nums[i], nums[j], nums[k]] such that their sum is 0.
        METHOD: O(n^2) Time, O(1) Space (excluding output). Sort array first. Iterate `i`, then use Two Pointers `l` and `r` to find the remaining sum.
        """
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # If current number is > 0, we can't sum to 0
            if a > 0:
                break
            
            # Skip duplicate first number
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # Skip duplicate second number (l) to avoid duplicate triplets
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                        
        return res

# --- Main Execution ---
if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: Standard case
    nums1 = [-1, 0, 1, 2, -1, -4]
    print(f"Test 1: {sol.threeSum(nums1)}") 
    # Expected: [[-1, -1, 2], [-1, 0, 1]]

    # Test Case 2: No solution
    nums2 = [0, 1, 1]
    print(f"Test 2: {sol.threeSum(nums2)}") 
    # Expected: []

    # Test Case 3: All zeros
    nums3 = [0, 0, 0]
    print(f"Test 3: {sol.threeSum(nums3)}") 
    # Expected: [[0, 0, 0]]