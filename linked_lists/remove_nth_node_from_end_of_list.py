from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Remove nth node from the end of list and return the head of modified list

        Args:
            head (ListNode): head of linkedlist
            n (integer): index of node to be removed from the end 

        Return: 
            listNode: head of modified list

        Time Complexity: O(n)
        Space Compleixty: O(1)

        we cannot know where is it without the end, must reach end
        we dont have a prev pointer, we either run 2 times or save pointer reference 
        which pointer to save?  array to save becaue at most 30

        reserve n nodes between two pointers, until the fast pointer reach the end
        """
        dummy = ListNode(0, head)
        slow, fast = dummy, dummy

        # fast = slow + n 
        for _ in range(n):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next 

        return dummy.next