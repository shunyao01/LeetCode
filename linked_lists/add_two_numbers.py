from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Add 2 numbers which are given in linkedlist in reverse order

        Args:
            l1: linkedlist 1
            l2: linkedlist 2

        Return:
            listnode: linkedlist of the sum of l1 and l2

        Time Complexity: O(n)
        Space Complexity: O(1)

        i=0 ones, i=1 tens, i=2 hundreds
        """
        dummy = ListNode()
        node = dummy
        carry = 0

        while l1 or l2 or carry:

            # total = l1 + l2 + carry forward
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry

            # udpate calculation
            carry = total // 10
            node.next = ListNode(val= total % 10)

            # update pointer
            node = node.next
            if l1: l1 = l1.next 
            if l2: l2 = l2.next 

        return dummy.next