from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Find answer where answer[i] is the product of all elements in array except for num[i]

        Args:
            list of positive integer

        Return:     
            product arrary

        Time Complexity: O(n)
        Space Complexity: O(1)

        Division: Handle zero division
        Prefix and Suffix
        """
        # track and exclude zero in multiplication
        prod = 1
        zero = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                prod *= nums[i]
            else: 
                zero += 1
        
        if zero > 1:
            return [0] * len(nums)

        # exclude zero in division
        for i, c in enumerate(nums):
            if zero: nums[i] = 0 if c else prod
            else: nums[i] = prod // c

        return nums

        # Prefix and suffix
        # res = [1] * len(nums)
        # prefix = 1
        # for i in range(len(nums)):
        #     res[i] = prefix
        #     prefix *= nums[i]
        
        # suffix = 1
        # for j in range(len(nums)-1, -1, -1):
        #     res[j] *= suffix
        #     suffix *= nums[j]
        
        # return res