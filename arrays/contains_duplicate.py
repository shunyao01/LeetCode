class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Check if the list contains duplicates 

        Args:
            List of integer

        Return:
            Boolean

        Time Complexity: O(n) 
        Space Complexity: O(1)
        """
        num_set = set()
        for n in nums:
            if n in num_set:
                return True
            num_set.add(n)
        return False