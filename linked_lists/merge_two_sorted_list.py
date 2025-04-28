from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merge two sorted linked list

        Args:
            list1: sorted linked list
            list2: sorted linked list 

        Return:
            listnode: the result linked list formed by merging list1 and list2

        Edge case:
            empty list
        """        
        start = ListNode()
        node = start

        while list1 and list2:

            # case list 1 > list 2
            if list1.val > list2.val:
                node.next = list2
                list2 = list2.next

            # case list 2 >= list 1
            elif list2.val >= list1.val:
                node.next = list1
                list1 = list1.next

            # print(start.next)
            node = node.next

        # case list 2 empty
        if not list2:
            node.next = list1

        # case list 1 empty
        elif not list1:
            node.next = list2
            
        return start.next