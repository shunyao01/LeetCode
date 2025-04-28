from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverse linked list

        Time Complexity: O(n)
        Space Complexity: O(1)

        Edge case: empty list
        """
        if not head: return None

        current = head
        prev = None
        
        # get the end
        while current:
            # update pointer
            nxt = current.next

            # update edge
            current.next = prev

            # udpate pointer
            prev = current 
            current = nxt

        return prev