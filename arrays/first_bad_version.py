# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
def isBadVersion(version: int) -> bool:
    return True

class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
        Binary Search to find the firstbadversion

        Args:
            n: integer which is the nuber of version
            
        Return
            bool: where the version is bad
        
        Time Complexity: O(log n * 2calls)
        Space Complexity: O(1)
        """
        mid = n//2
        low = 1
        high = n 
        
        while high > low:

            mid = (high + low) // 2 
            if not isBadVersion(mid): # mid good, go right
                low = mid + 1
            
            else: # mid bad
                high = mid - 1
        
        return low