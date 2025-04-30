from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Find two integers which add up to the target and return their indices given a sorted list
        
        Args:
            numbers: list of integers
            target: integer to add up to
        
        Return:
            list[int]: indexes + 1 of the numbers which add up to target

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        l, r = 0, len(numbers) - 1

        while r > l:
            x = numbers[l] + numbers[r]
            if x < target:
                l += 1
            elif x > target:
                r -= 1
            else:
                return [l+1, r+1]

        return []