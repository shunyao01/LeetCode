from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        Return True if the integer in nums array can be partitioned into two subsets with the same sum, else False

        Args:  
            array of integer

        Return: 
            boolean: if the array can be splited into 2 subsets with the same sum

        Time Complexity: O(n * target)
        Space Complexity: O(target)

        01 Knapsack Dynamic Programming: 
            dp[i] = true if a subset of the first i elements can be sum to j
            outer loop: integer
            inner loop: dp array

            size of dp is half of total sum
            prevent reusing by doing the loop backward
            Only need to find 1 valid combination is found, then the rest of the subset will also form another one
        """
        total = sum(nums)
        target = total//2

        # odd number means impossible
        if total % 2 != 0: return False

        # Initialize memo, max number will be half
        dp = [True] + [False] * target

        for n in nums:
            for j in range(len(dp)-1, n-1, -1):
                dp[j] = dp[j] or dp[j-n]

                if dp[target]:
                    return True

        return dp[target]