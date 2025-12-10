from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        PROBLEM: Reverse a singly linked list.
        METHOD: O(n) Time, O(1) Space. Iterative. Use `prev` and `curr` pointers. 
        Save `curr.next`, redirect `curr.next` to `prev`, then advance both.
        """
        prev = None
        curr = head
        
        while curr:
            next_node = curr.next  # Save next node
            curr.next = prev       # Reverse the link
            prev = curr            # Move prev forward
            curr = next_node       # Move curr forward
            
        return prev

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
    
    # Test Case 1: Standard list
    head1 = create_linked_list([1, 2, 3, 4, 5])
    reversed_head1 = sol.reverseList(head1)
    print(f"Test 1: {print_linked_list(reversed_head1)}") 
    # Expected: [5, 4, 3, 2, 1]

    # Test Case 2: Two elements
    head2 = create_linked_list([1, 2])
    reversed_head2 = sol.reverseList(head2)
    print(f"Test 2: {print_linked_list(reversed_head2)}") 
    # Expected: [2, 1]

    # Test Case 3: Empty list
    head3 = create_linked_list([])
    reversed_head3 = sol.reverseList(head3)
    print(f"Test 3: {print_linked_list(reversed_head3)}") 
    # Expected: []