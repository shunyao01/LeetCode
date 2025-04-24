from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Group the anagram from strs and return list of groups

        Args:
            strs: non-empty list of strings where 0<=len(strs[i])<=100 and strs[i] has lowercase letters

        Return:
            List of list of strings representing groups of anagrams

        Integer Array [0]*26
        For each group of anagram we need 1 integer array

        Naive: Loop through strs, nested loop to check anagram, O(n^2)
               For each string, sort them, such that anagrams in the same group become the same string
        
        Trick: HashMap (anagram groups have the same key), integer array to skip sort

        Time Complexity: O(m*n)
        Space Complexity: O(m)
        """
        # initialize int array size n or nxn, int_arr[i] = no of occurrence of char[i] in str
        str_dict = defaultdict(list)

        # Optimize: use integer arrray to replace sort
        for s in strs:
            
            # Initialize integer array
            integer_arr = [0] * 26 
            # Change string to interger array format
            for c in s:
                integer_arr[ord(c)-ord("a")] += 1
            
            # Use integer array as a hash key using tuple(list)
            str_dict[tuple(integer_arr)].append(s)

        return list(str_dict.values())

        # Naive
        # # sort the strings
        # for s in strs:
        #     sorted_s = ''.join(sorted(s))
        #     if sorted_s not in str_dict:
        #         str_dict[sorted_s] = []
        #     str_dict[sorted_s].append(s)

        # return list(str_dict.values())