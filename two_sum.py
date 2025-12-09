def two_sum(nums: list[int], target: int) -> list[int]:
    """
    PROBLEM: Find indices of two numbers in `nums` summing to `target`.
    METHOD: O(n) One-pass Hash Map. Check if `target - num` exists in visited map; if not, store `num -> index`.
    """
    seen = {} # Maps value to index
    
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
        
    return []