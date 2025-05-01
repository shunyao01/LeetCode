from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Perform search on 2d matrix and return index of the target

        Args:
            matrix: 2d matrix of integers
            target: number to be searched

        Return:
            bool: if target is found

        Time Complexity: O(log mn)
        Space Complexity: O(1)
        """
        if not matrix: return False
        
        total = len(matrix) * len(matrix[0])
        low = 0
        high = total - 1
        
        while low <= high:

            # get mid index, convert index to 2d
            mid = (low + high) // 2
            i = mid // len(matrix[0]) 
            j = mid % len(matrix[0]) 

            print(total, i, j, mid)

            if matrix[i][j] > target:
                high = mid - 1
            elif matrix[i][j] < target:
                low = mid + 1
            else: # found
                return True

        return False
        