from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Check if t is an anagram of s

        Args:
            s: string
            t: string, potential anagram
        
        Return:
            boolean, if t is an anagram

        Record number of occurrence of each character in string t
        Check if all characters in string t are used up
        
        Hash Table or Integer Array

        Time Complexity: O(n)
        """
        count = [0] * 26 

        # record occurrence of t into hashmap
        for chr in t:
            count[ord(chr) - ord('a')] += 1

        # loop s and minus the occurence 
        for chr in s:
            count[ord(chr) - ord('a')] -= 1

        # check if all occurrence are same
        return all(c == 0 for c in count)