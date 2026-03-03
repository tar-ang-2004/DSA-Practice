#Merge Two Sorted Lists Problem

# Problem Statement: You are given the heads of two sorted linked lists list1 and list2. Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists. Return the head of the merged linked list.

# Example:
# Given list1 = [1,2,4] and list2 = [1,3,4],
# The merged list is [1,1,2,3,4,4].

class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        current = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # If there are remaining nodes in either list, append them
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        
        return dummy.next
    
if __name__ == "__main__":
    # Create first linked list 1 -> 2 -> 4
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)

    # Create second linked list 1 -> 3 -> 4
    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)

    # Merge the two linked lists
    result = Solution().mergeTwoLists(list1, list2)

    # Print the merged linked list
    current = result
    while current:
        print(current.val, end=" ")
        current = current.next

# Time Complexity: O(n + m), where n and m are the number of nodes in list1 and list2, respectively. We traverse both lists once.
# Space Complexity: O(1), as we are using only a constant amount of extra space