from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Return all possible combinations given the digits and alphabets

        Args:
            digits(string): integer 2-9 representing the possible characters it can form

        Return:
            list of string: all possible combinations of the characters

        Time Complexity: O(4^n)
        Space Complexity: O(n)

        Trick: backtrack (recursive) vs queue (iterative)
        """
        if not digits:
            return []

        # conversion
        letter_dict = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        res = []

        def backtrack(path, index):
            # if full combination, append 
            if len(path) == len(digits):
                res.append(path)
                return 
            # if not, take the current path, add character and proceed
            for char in letter_dict[digits[index]]:
                backtrack(path + char, index+1)

        backtrack("", 0)

        return res