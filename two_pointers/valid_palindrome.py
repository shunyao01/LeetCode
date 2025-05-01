class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Check if only have 1 odd number of frequency
        
        Args:
            s: string

        Return:
            boolean

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not s: return True

        l, r = 0, len(s)-1

        while r > l:

            while l < r and not s[l].isalnum(): l += 1
            while l < r and not s[r].isalnum(): r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True
