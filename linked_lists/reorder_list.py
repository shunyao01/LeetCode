from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        Reorder the list to such sequence [0, n, 1, n-1, 2, n-2]

        Args:
            head (listNode): head of the linkedlist with integer values

        Return:
            None
        
        Time Complexity: O(n)
        Space Complexity: O(1)

        Tricks:
            Find middle
            Split into two sorted list and reverse the second one
            Merge the list
        """
        # edge case
        if not head or not head.next:
            return 

        # initialize
        node = head
        mid = head

        # get middle point 
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # split to 2 lists
        lst2 = slow.next
        slow.next = None

        # reverse linkedlist lst2
        prev = None
        node = lst2
        while node:
            nxt = node.next
            node.next = prev

            prev = node
            node = nxt

        # # merge list
        lst1 = head
        lst2 = prev 

        while lst2: # lst2 is shorter
            nxt1 = lst1.next 
            nxt2 = lst2.next

            lst1.next, lst2.next = lst2, lst1.next # modify

            lst1 = nxt1
            lst2 = nxt2

        return head
