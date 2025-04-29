from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Perform binary search 

        ArgsL
            nums: list of integer
            target: integer to be found

        Return:
            int: index of the found target or -1 if not found
        """
        low, high = 0, len(nums)-1

        while low <= high:
            mid = (low + high) // 2
            
            # case 1: mid = target
            if nums[mid] == target: return mid
            # case 2: mid > target, go left
            elif nums[mid] > target: high = mid - 1
            # case 3: mid < target, go right
            else: low = mid + 1

        return -1 # not found
