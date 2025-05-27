from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Find duplicated number in nums

        Args:
            nums: array of size n+1 where nums[i] is in [1,n]

        Time Compleixity: O(n)
        Space Complexity: O(1)

        Negative Mark: Use index to mark value
        Fast and Slow: Finding duplicates is like finding cycle, each value is a pointer to next node
                       Floyd’s Tortoise and Hare (Cycle Detection)

        Binary Search nlogn
        """
        slow, fast = nums[0], nums[0]

        # detect cycle, intersection point
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # find entry point p=x, distance between start-cycle and cycle-intersect same
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow
        
        # i = 0 

        # for i in range(len(nums)):
            
        #     index = abs(nums[i])-1

        #     # check if repeated
        #     if nums[index] < 0: return abs(nums[i])

        #     # if not, mark the value index negative
        #     nums[index] *= -1

        # return -1
