from typing import List
w
class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Compute how much water can the map trap given the map height in list form and width = 1

        Args:
            height: list of integer represnting height of bar

        Return:
            int: amount of water that can be trap
       
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        l, r = 0, len(height)-1
        max_l, max_r = height[l], height[r]
        water = 0

        # Use two pointers to traverse from both ends.
        # At each step, move the pointer with the smaller max height inward,
        # and accumulate trapped water at that position.
        while l < r:
            if max_l < max_r: 
                l += 1
                max_l = max(height[l], max_l)
                water += max_l - height[l]
            else:
                r -= 1
                max_r = max(height[r], max_r)
                water += max_r - height[r]


        return water
