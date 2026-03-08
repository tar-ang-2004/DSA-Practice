#Reorder List Problem

# Problem Statement: Given the head of a singly linked list, reorder the list to follow the pattern: L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …

# Example:
# Given head = [1,2,3,4],
# The reordered list is [1,4,2,3].

class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next:
            return
        
        # Step 1: Find the middle of the linked list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half of the linked list
        prev = None
        current = slow
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        # Step 3: Merge the two halves
        first_half = head
        second_half = prev
        
        while second_half.next:
            temp1 = first_half.next
            temp2 = second_half.next
            
            first_half.next = second_half
            second_half.next = temp1
            
            first_half = temp1
            second_half = temp2

if __name__ == "__main__":
    # Create a linked list 1 -> 2 -> 3 -> 4
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)

    # Reorder the linked list
    Solution().reorderList(head)

    # Print the reordered linked list
    current = head
    while current:
        print(current.val, end=" ")
        current = current.next

# Time Complexity: O(n), where n is the number of nodes in the linked list. We traverse the list a few times, but each traversal is O(n).
# Space Complexity: O(1), as we are using only a constant amount of extra space