from typing import List
import math 

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Interpret the tokens using reverse polish notation and return the value of the expression

        Args:
            tokens: list of strings containing operators or integer

        Return:
            int: value of the expression
        
        Time Complexity: O(n)
        Space Complexity: O(n)

        Trick: FIFO stack for interger, immediate resolve operator
        """
        if not tokens: return 
        if len(tokens) == 1: return int(tokens[0])

        res = None
        integer_stack = []

        for s in tokens:
            
            if s.lstrip('-').isdigit(): # add digits
                integer_stack.append(s)
            
            else: # resolve operator

                if res is None: # first time, get the right, res = l # r
                    res = int(integer_stack.pop())
                n = int(integer_stack.pop())
                
                if s == '+':
                    res += n
                elif s == '-':
                    res = n - res # left - right
                elif s == '*':
                    res *= n
                elif s == '/':
                    res = math.trunc(n / res) # left / right, // is math.floor, use trunc
                    
        return res
