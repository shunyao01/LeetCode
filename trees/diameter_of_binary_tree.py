from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Perform dfs from root, update the height, max diameter = left + right

        Time Complexity: O(n)
        Space Complexity: O(log n) due to recursion stack
        """
        self.diameter = 0

        def dfs(node):
            """DFS and return height"""
            if not node: return 0
            
            # get left and right height, calculate diameter = left + right
            left = dfs(node.left)
            right = dfs(node.right)
            self.diameter = max(self.diameter, left + right)

            return 1 + max(left, right)

        dfs(root)
        return self.diameter