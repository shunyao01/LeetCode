from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Given list of integer temperatures, return answer such that n is the number of days left to a wartmer temperature

        Args:
            temperature (list[int]): list of temperatures

        Return: 
            answer (list[int]): number of days until warmer temperature

        Time Complexity: O(n)
        Space Complexity: O(n)

        Trick: monotonic decreasing stack, decrease from bottom to top of the stack
        """
        n = len(temperatures)
        max_stack = []
        res = [0] * n

        # loop thorugh and find warmer with stack
        for i in range(n):

            while max_stack and temperatures[i] > temperatures[max_stack[-1]]: # found warmer
                left = max_stack.pop()
                res[left] = i - left

            max_stack.append(i)
            
        return res 