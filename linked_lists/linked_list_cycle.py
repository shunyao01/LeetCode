from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Check if a linked list has cycle
        
        Args:
            head: starting node in linked list

        Return:
            boolean value indicating presence of cycle

        Time Complexity: O(n)
        Space Complexity: O(1)

        pos = index the tail 's next is connected to 

        Trick: use a marked attribute in listnode, use val in this case 

        Alternative: fast and slow pointers (Floyd's Cycle Detection Algorithm)
        """
        if not head: return False

        # Fast and Slow
        slow = head
        fast = head

        while fast.next and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

        # node = head

        # pos = 0
        # while node.next is not None:
        #     node.val = None # mark current node
        #     node = node.next # move to next node
        #     pos += 1

        #     # cycle detected if val is None
        #     if node.val is None:
        #         return True

        # # no cycle detected
        # pos = -1
        # return False
