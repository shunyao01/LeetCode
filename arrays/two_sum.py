from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Find the two indices in nums which adds up to the target value

        This method iterates through num and record index of each num and check if the complement of the current num is observed already

        Args:
            nums (List[int]): A list of integers
            target (int): An integer, target sum

        Returns:
            List[Int]: A list containing two indices which correspond to two values in nums, in which they add up to the target value

        num_map[n] = i where n is the value of current num, i is the index of the n in nums
        """
        num_map = {}
        for i, n in enumerate(nums):
            complement = target - n 
            if complement in num_map:
                return [num_map[complement], i]
            num_map[n] = i

        return []