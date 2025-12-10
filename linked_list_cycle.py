from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        PROBLEM: Determine if the linked list has a cycle in it.
        METHOD: O(n) Time, O(1) Space. Floyd's Cycle Finding Algorithm (Fast & Slow Pointers).
        `slow` moves 1 step, `fast` moves 2 steps. If they collide, there is a cycle. If `fast` reaches end, no cycle.
        """
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next          # Move 1 step
            fast = fast.next.next     # Move 2 steps
            
            if slow == fast:
                return True           # Collision -> Cycle detected
                
        return False                  # Reached null -> No cycle

# --- Main Execution ---
if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: Cycle exists (3 -> 2 -> 0 -> -4 -> 2...)
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # Cycle back to node 2
    
    print(f"Test 1: {sol.hasCycle(node1)}") # Expected: True

    # Test Case 2: No cycle (1 -> 2)
    nodeA = ListNode(1)
    nodeB = ListNode(2)
    nodeA.next = nodeB
    
    print(f"Test 2: {sol.hasCycle(nodeA)}") # Expected: False

    # Test Case 3: Single node
    nodeX = ListNode(1)
    print(f"Test 3: {sol.hasCycle(nodeX)}") # Expected: False