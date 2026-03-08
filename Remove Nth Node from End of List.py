#Remove Nth Node from End of List Problem

# Problem Statement: Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Example:
# Given head = [1,2,3,4,5] and n = 2,
# The linked list after removing the second node from the end is [1,2,3,5].

class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        
        # Move first pointer n+1 steps ahead
        for _ in range(n + 1):
            first = first.next
        
        # Move both pointers until first reaches the end
        while first:
            first = first.next
            second = second.next
        
        # Remove the nth node from the end
        second.next = second.next.next
        
        return dummy.next
    
if __name__ == "__main__":
    # Create a linked list 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    n = 2
    result = Solution().removeNthFromEnd(head, n)

    # Print the linked list after removal
    current = result
    while current:
        print(current.val, end=" ")
        current = current.next
    print()  # For a newline after printing the list

# Time Complexity: O(n), where n is the number of nodes in the linked list. We traverse the list at most twice.
# Space Complexity: O(1), as we are using only a constant amount of extra space