from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Find the number of car fleet, which is the number of times one car or multiplen car reach driving next to each other and reach target together.

        Args:
            target (int): The distance to the target, in miles.
            position (List[int]): A list of integers where each value represents the initial position of a car on the road.
            speed (List[int]): A list of integers where each value represents the speed of the car at the corresponding position.

        Returns:
            int: The total number of fleets, where each fleet consists of cars that reach the target at the same time.

        Time Complexity: O(n log n)
        Space Complexity: O(n)

        Trick: next greater element (time), the car takes new fleet if the time if longer than the front
        """
        n = len(position)

        # time taken
        time = [(target-p)/s for p, s in zip(position, speed)]

        # sort based on position, car from the back cannot pass car in front
        paired = sorted(zip(position, time), reverse=True)

        stack = []
        for p, t in paired:
            if not stack or t > stack[-1]:
                stack.append(t) 

        return len(stack)