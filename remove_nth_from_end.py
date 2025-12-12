from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        PROBLEM: Remove the n-th node from the end of the list and return its head.
        METHOD: O(L) Time, O(1) Space. One-pass Two Pointers. 
        1. Use a dummy node pointing to head. 
        2. Move `right` pointer `n` steps ahead.
        3. Move both `left` and `right` until `right` reaches end. `left` is now before the target.
        4. Skip the target node.
        """
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        # Step 1: Advance right pointer by n steps
        while n > 0 and right:
            right = right.next
            n -= 1
            
        # Step 2: Move both pointers until right reaches the end
        while right:
            left = left.next
            right = right.next
            
        # Step 3: Delete the node
        # left is now at the node BEFORE the one we want to delete
        left.next = left.next.next
        
        return dummy.next

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
    
    # Test Case 1: Standard case (Remove 2nd from end: 4)
    head1 = create_linked_list([1, 2, 3, 4, 5])
    res1 = sol.removeNthFromEnd(head1, 2)
    print(f"Test 1: {print_linked_list(res1)}") 
    # Expected: [1, 2, 3, 5]

    # Test Case 2: Remove head (n = length)
    head2 = create_linked_list([1, 2])
    res2 = sol.removeNthFromEnd(head2, 2)
    print(f"Test 2: {print_linked_list(res2)}") 
    # Expected: [2] (Node 1 removed)

    # Test Case 3: Remove single element
    head3 = create_linked_list([1])
    res3 = sol.removeNthFromEnd(head3, 1)
    print(f"Test 3: {print_linked_list(res3)}") 
    # Expected: []