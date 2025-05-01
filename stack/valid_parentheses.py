class Solution:
    def isValid(self, s: str) -> bool:
        """
        Check if given string has valid parentheses
        
        Args:
            s: string containing parentheses

        Return:
            bool: True if string is valid

        Use a stack, LIFO for open bracket

        Edge case:
            empty string
            string length 1
            open bracket > close bracket
            close bracket > open bracket

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        map = {')':'(', '}':'{', ']':'[' }
        stack = []

        for b in s:
            # meet open bracket: add open bracket to stack
            if b in map.values(): stack.append(b)

            # meet close bracket: pop from stack and check
            elif b in map:
                if not stack: return False # no open bracket, found close bracket
                if map[b] != stack.pop(): return False # check valid corresponding bracket

        return not stack # no close bracket, found open bracket, then false