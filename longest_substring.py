class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        PROBLEM: Find the length of the longest substring without repeating characters.
        METHOD: O(n) Time, O(min(n, m)) Space. Sliding Window with Hash Set. 
        Expand `r`, if duplicate found, shrink `l` until valid. Update max length.
        """
        char_set = set()
        l = 0
        res = 0
        
        for r in range(len(s)):
            # If current char is already in set, shrink window from left
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            
            # Add current char and update result
            char_set.add(s[r])
            res = max(res, r - l + 1)
            
        return res

# --- Main Execution ---
if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: Standard case
    s1 = "abcabcbb"
    print(f"Test 1 ('{s1}'): {sol.lengthOfLongestSubstring(s1)}") # Expected: 3 ("abc")

    # Test Case 2: All same characters
    s2 = "bbbbb"
    print(f"Test 2 ('{s2}'): {sol.lengthOfLongestSubstring(s2)}") # Expected: 1 ("b")

    # Test Case 3: Tricky case (answer is in the middle)
    s3 = "pwwkew"
    print(f"Test 3 ('{s3}'): {sol.lengthOfLongestSubstring(s3)}") # Expected: 3 ("wke")