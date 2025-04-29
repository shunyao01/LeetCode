from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Merge list of sorted linked list to one sorted linked list

        Args:
            lists: list of sorted linked list filled with integers

        Return:
            listNode: One combined sorted linked list of the lists

        Time Complexity: O(N*logk)
        Space Complexity: O(k)
        where k is the number of list in lists, N is the total number of numbers, N=n*k

        Tricks: Divide and conquer
        """
        if not lists or len(lists) == 0: return None # len 0
        if len(lists) == 1: return lists[0] # len 1
 
        # len >= 2
        mid = len(lists) // 2
        lst1 = self.mergeKLists(lists[:mid])
        lst2 = self.mergeKLists(lists[mid:])

        return self.merge(lst1, lst2)

    def merge(self, lst1: List[Optional[ListNode]], lst2: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Merge 2 sorted linked list 
        """
        dummy = ListNode()
        node = dummy

        while lst1 and lst2: # both not empty, O(k) per iter

            # lst1 <= lst2
            if lst1.val <= lst2.val:
                node.next = lst1
                lst1 = lst1.next
                
            else:
                node.next = lst2
                lst2 = lst2.next

            node = node.next

        if lst1: # lst 2 empty
            node.next = lst1
        else: # lst 1 empty
            node.next = lst2

        return dummy.next