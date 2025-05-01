from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Return length of the longest consecutive elements sequence

        Args:
            nums: unsorted list of integer

        Return:
            int: length of longest consecutive sequence

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # use set
        num_set = set(nums)
        max_seq = 0
        
        for num in nums: # for each potential sequence middle, search left and right
            if num not in num_set: # explored, skip
                continue
            num_set.remove(num) # mark as explored

            cur_len = 1
            left, right = num - 1, num + 1

            while left in num_set:
                num_set.remove(left)
                left -= 1
                cur_len += 1

            while right in num_set:
                num_set.remove(right)
                right += 1
                cur_len += 1

            max_seq = max(max_seq, cur_len)

        return max_seq

        # better
        # numSet = set(nums)
        # longest = 0

        # for num in numSet:
        #     if (num - 1) not in numSet: # make sure it is starting point, then expand +1
        #         length = 1
        #         while (num + length) in numSet:
        #             length += 1
        #         longest = max(length, longest)
        # return longest