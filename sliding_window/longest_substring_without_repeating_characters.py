class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Find the length of the longest substring in string s without duplicate characters

        Args:
            s: a string
        
        Return:
            an integer representing length of longest substring
        
        Edge case: 
            len(s) = 0
            len(s) = 1

        Naive solution - brute force O(n), compare longest substring starting from ith character in strong s where 0 <= i < len(s)
        Trick(Set, Hash) - record index in hashmap, use left right pointer for sliding window, after repeating character is met, slide through it

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        max_len = 0
        left = 0
        hm = {}

        # loop through substring starting from each character
        for right in range(len(s)):
            
            if s[right] not in hm or hm[s[right]] < left: # no repeating character in valid substring, increment length and record the char in hm
                hm[s[right]] = right
                max_len = max(max_len, right - left + 1)
            else: #  repeating character met, move left pointer to the right of the repeating character on the left
                left = hm[s[right]] + 1
                hm[s[right]] = right

        return max_len
        
        ### Naive solution
        # max_len = 0

        # # loop through substring starting from each character
        # for i in range(len(s)):
            
        #     # reset hashmap and current length
        #     hm = {}
        #     current_len = 0

        #     # starting from ith character, iterate and increment current length until a repeating character is met
        #     for j in range(i, len(s)):
        #         if s[j] not in hm: # increment length and record the char in hm
        #             hm[s[j]] = 
        #             current_len += 1
        #         else: #  repeating character met, exit loop and compare current length with max length
        #             break
        #     max_len = max(max_len, current_len)

        # return max_len
        
