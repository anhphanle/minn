class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        PROBLEM: Determine if `s` reads the same forward and backward.
        METHOD: O(n) Time, O(1) Space. Two Pointers. Move inward from both ends, skipping non-alphanumeric chars.
        """
        l, r = 0, len(s) - 1
        
        while l < r:
            # Skip non-alphanumeric characters from left
            if not s[l].isalnum():
                l += 1
                continue
            
            # Skip non-alphanumeric characters from right
            if not s[r].isalnum():
                r -= 1
                continue
            
            # Compare characters
            if s[l].lower() != s[r].lower():
                return False
            
            # Move pointers inward
            l += 1
            r -= 1
            
        return True

# --- Main Execution ---
if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: Standard palindrome
    s1 = "A man, a plan, a canal: Panama"
    print(f"Test 1: {sol.isPalindrome(s1)}") # Expected: True
    
    # Test Case 2: Not a palindrome
    s2 = "race a car"
    print(f"Test 2: {sol.isPalindrome(s2)}") # Expected: False

    # Test Case 3: Empty or spaces only
    s3 = " "
    print(f"Test 3: {sol.isPalindrome(s3)}") # Expected: True (Empty string is valid)