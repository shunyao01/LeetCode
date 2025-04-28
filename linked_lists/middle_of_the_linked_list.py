from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Given head of linked list, return the moddile node, return second middle node if there are two

        Args:
            head: first node of linked list
        
        Return:
            the middle node

        Two pointer, one determining the end, one represent middle, Floyd
        """
        mid, end = head, head

        while end.next is not None:
            
            # head will always proceed
            mid = mid.next
            
            # traverse 2 havent reach end else traverse 1 
            if end.next.next is not None:
                end = end.next.next
            else:
                end = end.next

        return mid