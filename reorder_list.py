from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        PROBLEM: Reorder list to L0 -> Ln -> L1 -> Ln-1... in-place.
        METHOD: O(n) Time, O(1) Space. Three steps:
        1. Find middle (Slow/Fast pointers). Split list into two halves.
        2. Reverse the second half.
        3. Merge the two halves alternately.
        """
        if not head: return 
        
        # Step 1: Find middle using Slow/Fast pointers
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Split the list into two halves
        second = slow.next
        slow.next = None # Cut off the end of first half
        
        # Step 2: Reverse the second half
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
            
        # Step 3: Merge two halves (first half: head, second half: prev)
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

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
    
    # Test Case 1: Even length (1 -> 2 -> 3 -> 4)
    head1 = create_linked_list([1, 2, 3, 4])
    sol.reorderList(head1)
    print(f"Test 1: {print_linked_list(head1)}") 
    # Expected: [1, 4, 2, 3]

    # Test Case 2: Odd length (1 -> 2 -> 3 -> 4 -> 5)
    head2 = create_linked_list([1, 2, 3, 4, 5])
    sol.reorderList(head2)
    print(f"Test 2: {print_linked_list(head2)}") 
    # Expected: [1, 5, 2, 4, 3]