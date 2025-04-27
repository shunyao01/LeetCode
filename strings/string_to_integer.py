class Solution:
    def myAtoi(self, s: str) -> int:
        """
        Convert string to a 32 bit integer
        
        Ignore space 
        +- sign
        Skip leading zero 
        Round

        Args:
            s: string representing the string form of integer and need preprocessing

        Return:
            corresponding integer value

        Edge case:
            Empty string
            length string 0
            0 for invalid string
            Round to range within [-231, 231 - 1]
        """
        # Whitespace
        s = s.strip()

        # if len(S) = 0
        if not s:
            return 0

        sign, i, res = 1, 0, 0
        
        # check sign in first chr, if sign detected, modify sign, skip first chr
        if s[0] == "-":
            sign = -1
            i += 1
        elif s[0] == "+":
            i += 1

        # invalid chr case
        while i < len(s) and s[i].isdigit():
            
            c = s[i]
            i += 1

            # Leading Zero
            # Conversion, now it falls under 0-9, *10 and add next digit
            res *= 10
            res += ord(c) - ord("0")

            # Rounding
            if res*sign > 2**31 - 1:
                return 2**31 - 1
            elif res*sign < -2**31:
                return -2**31
            
        return res*sign