class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Find longest palindrome in string s

        Args:
            s: string 

        Return:
            longest palindrome in s

        Time Complexity: O(n^2)
        Space Complexity: O(1)

        Find each potential palindrome middle point + Compare left and right using previously computed result

        Tricks: Manacher’s Algorithm O(n)
        Ours: Expand from center O(n^2), O(1), functional programming
        ALternative: Dynamic Programming O(n^2), O(n^2)
        """
        longest_l, longest_r = 0, 0

        def expand_around_center(l, r):
            while l>=0 and r<len(s) and s[l] == s[r]:
                # Increment
                l -= 1
                r += 1
            return l+1, r-1

        # Loop starting point
        for i in range(len(s)):
            odd_l, odd_r = expand_around_center(i, i)
            even_l, even_r = expand_around_center(i, i+1)

            # update max
            if odd_r - odd_l + 1 > longest_r - longest_l:
                longest_l, longest_r = odd_l, odd_r
            if even_r - even_l + 1 > longest_r - longest_l:
                longest_l, longest_r = even_l, even_r

        # Identify longest palindrome index
        return s[longest_l:longest_r+1]