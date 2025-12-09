class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        PROBLEM: Determine if `t` is a rearrangement of `s`.
        METHOD: O(n) Hash Map. Count chars in `s`, decrement for `t`. Ensure counts match.
        """
        if len(s) != len(t):
            return False
        
        count = {}
        
        # Step 1: Count frequency of chars in s
        for char in s:
            count[char] = count.get(char, 0) + 1
            
        # Step 2: Decrement frequency for chars in t
        for char in t:
            if char not in count or count[char] == 0:
                return False
            count[char] -= 1
            
        return True

# --- Main Execution ---
if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1
    s1, t1 = "anagram", "nagaram"
    print(f"Test 1 ('{s1}', '{t1}'): {sol.isAnagram(s1, t1)}") # Expected: True
    
    # Test Case 2
    s2, t2 = "rat", "car"
    print(f"Test 2 ('{s2}', '{t2}'): {sol.isAnagram(s2, t2)}") # Expected: False

    # Test Case 3 (Different lengths)
    s3, t3 = "ab", "a"
    print(f"Test 3 ('{s3}', '{t3}'): {sol.isAnagram(s3, t3)}") # Expected: False