#Linked List Cycle Problem

# Problem Statement: Given head, the head of a linked list, determine if the linked list has a cycle in it.

# Example:
# Given head = [3,2,0,-4], pos = 1,
# There is a cycle in the linked list, where the tail connects to the second node (0-indexed). Return true.

class ListNode:
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        
        return False
    
if __name__ == "__main__":
    # Create a linked list 3 -> 2 -> 0 -> -4, with a cycle connecting back to the second node (2)
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next  # Create the cycle

    result = Solution().hasCycle(head)
    print(result)

# Time Complexity: O(n), where n is the number of nodes in the linked list. In the worst case, we might traverse the entire list.
# Space Complexity: O(1), as we are using only a constant amount of extra space