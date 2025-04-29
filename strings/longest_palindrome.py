class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        Find longest palindrome in string s

        Args:
            s: string 

        Return:
            length of longest palindrome that can be formed by characters in s

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        hashmap = {}
        mid_available = True # can only use 1 odd in the middle
        count = 0

        for c in s:
            hashmap[c] = hashmap.get(c, 0) + 1 
        
        for v in hashmap.values():
            if v%2 == 0: # even
                count += v
            else: # odd
                count += v-1
                if mid_available:
                    count += 1
                    mid_available = False

        return count