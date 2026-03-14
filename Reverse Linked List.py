#Reversed Linked List Problem

# Problem Statement: Given the head of a singly linked list, reverse the list, and return the reversed list.

# Example:
# Given head = [1,2,3,4,5],
# The reversed list is [5,4,3,2,1].

class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:

    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
    
if __name__ == "__main__":
    # Create a linked list 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    # Reverse the linked list
    result = Solution().reverseList(head)

    # Print the reversed linked list
    current = result
    while current:
        print(current.val, end=" ")
        current = current.next

# Time Complexity: O(n), where n is the number of nodes in the linked list. We traverse the list once.
# Space Complexity: O(1), as we are using only a constant amount of extra space