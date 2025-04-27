from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Find max area, by finding max(min height of two bar x width)
        Maximize x * min(yi, yj)

        Args:
            height: list containing integers which are height of the bar

        Return:
            Max area (x*y)

        Trick: Greedy, improve the bottleneck 
        Sliding Window? DP? Greedy? Two Pointer? 

        Because of the nature that the height is dependent on the lower bar,
        It does not matter how high one can go without improving the another
        if e=8, s=2 is better than s=1. Does that mean we will never look back to s=1?
        """
        # base case: start with biggest potential
        s, e = 0, len(height)-1

        # func to calculate height x * y
        max_area = (e-s) * min(height[e], height[s])

        # ending case
        while e > s:

            # if s shorter
            if height[s] < height[e]:
                s += 1
            # if e shorter or same
            else:
                e -= 1

            # check if new area is bigger
            area = (e-s) * min(height[e], height[s])
            max_area = max(area, max_area)

        return max_area