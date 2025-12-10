from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        PROBLEM: Find the middle node of the linked list. If there are two middle nodes, return the second one.
        METHOD: O(n) Time, O(1) Space. Fast & Slow Pointers. `slow` moves 1 step, `fast` moves 2 steps. When `fast` reaches end, `slow` is at middle.
        """
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next          # Move 1 step
            fast = fast.next.next     # Move 2 steps
            
        return slow

# --- Main Execution ---
def create_linked_list(arr):
    if not arr: return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def print_linked_list(head):
    vals = []
    curr = head
    while curr:
        vals.append(curr.val)
        curr = curr.next
    return vals

if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: Odd number of nodes (1, 2, 3, 4, 5) -> Middle is 3
    head1 = create_linked_list([1, 2, 3, 4, 5])
    mid1 = sol.middleNode(head1)
    print(f"Test 1: {print_linked_list(mid1)}") 
    # Expected: [3, 4, 5] (Output starts from middle node)

    # Test Case 2: Even number of nodes (1, 2, 3, 4, 5, 6) -> Middle is 4
    head2 = create_linked_list([1, 2, 3, 4, 5, 6])
    mid2 = sol.middleNode(head2)
    print(f"Test 2: {print_linked_list(mid2)}") 
    # Expected: [4, 5, 6]

    # Test Case 3: Single node
    head3 = create_linked_list([1])
    mid3 = sol.middleNode(head3)
    print(f"Test 3: {print_linked_list(mid3)}") 
    # Expected: [1]