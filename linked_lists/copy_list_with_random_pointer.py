from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        Return the head of the deep copy of the list

        Args:
            head (Node): first node of the original list

        Return:
            Node: deep copy of the list given

        Time Complexity: O(n)
        Space Complexity: O(1)

        Trick: keep track of pointers to old nodes (trick or hash) to avoid creating duplicating node during random & next
        A -> A' -> B -> B'
        """
        if not head: return 

        # copy and create node with value and nxt first
        node = head
        while node:
            nxt = node.next
            
            # clone node
            node.next = Node(node.val, next=nxt)
            node = nxt

        # copy the random pointer
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next # copy random
            curr = curr.next.next # iterate

        # recreate the cloned list
        node = head.next
        while node.next:
            node.next = node.next.next
            node = node.next

        return head.next