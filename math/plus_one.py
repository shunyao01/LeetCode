from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Given a list of digits, plus one and return result array of digits
        """
        carry = 1
        i = len(digits) - 1
        while carry > 0:

            # prepend 0
            if i == -1:
                digits.insert(0, 0)
                i += 1 

            val = digits[i] + carry
            carry = val // 10
            digits[i] = val % 10
            i -= 1
            
        return digits