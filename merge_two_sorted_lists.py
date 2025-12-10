from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        PROBLEM: Merge two sorted linked lists into one sorted list.
        METHOD: O(n + m) Time, O(1) Space. Iterative with Dummy Node. Compare heads of both lists, append smaller node to tail, advance pointer.
        """
        dummy = ListNode()
        tail = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
            
        # Attach the remaining part of the non-empty list
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
            
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
    
    # Test Case 1: Standard merge
    l1 = create_linked_list([1, 2, 4])
    l2 = create_linked_list([1, 3, 4])
    merged = sol.mergeTwoLists(l1, l2)
    print(f"Test 1: {print_linked_list(merged)}") 
    # Expected: [1, 1, 2, 3, 4, 4]

    # Test Case 2: One list empty
    l3 = create_linked_list([])
    l4 = create_linked_list([0])
    merged2 = sol.mergeTwoLists(l3, l4)
    print(f"Test 2: {print_linked_list(merged2)}") 
    # Expected: [0]

    # Test Case 3: Both empty
    l5 = create_linked_list([])
    l6 = create_linked_list([])
    merged3 = sol.mergeTwoLists(l5, l6)
    print(f"Test 3: {print_linked_list(merged3)}") 
    # Expected: []