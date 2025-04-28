from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Return non-repeating triplets such that three numbers add up to 0

        Args:
            nums: list of integer

        Return:
            index of triples that add up to 0

        two pointer expanding from zero
        no duplicates triplets, but duplicate element is allowed

        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        nums.sort()
        res = []

        for i in range(len(nums)):
            
            if nums[i] > 0: break
            if i - 1 >= 0 and nums[i] == nums[i-1]: continue # avoid duplicate i
        
            j, k = i + 1, len(nums) - 1

            while j < k:
                threesum = nums[i] + nums[j] + nums[k]
                if threesum == 0: 
                    res.append([nums[i], nums[j], nums[k]])

                    # move both pointers to skip duplicates j aand k
                    j += 1
                    k -= 1
                    
                    while j < k and nums[j] == nums[j-1]: # avoid duplicate j
                        j += 1
                    while j < k and nums[k] == nums[k+1]: # avoid duplicate k
                        k -= 1
                
                elif threesum > 0: 
                    k -= 1
                elif threesum < 0: 
                    j += 1 

        return res