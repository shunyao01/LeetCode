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
               Result is left or right
        """
        integer_stack = []

        for s in tokens:
            
            if s.lstrip('-').isdigit(): # add digits
                integer_stack.append(int(s))
            
            else: # resolve operator

                r = integer_stack.pop()
                l = integer_stack.pop()
                
                if s == '+':
                    temp = l + r
                elif s == '-':
                    temp = l - r # left - right
                elif s == '*':
                    temp = l * r
                elif s == '/':
                    temp = math.trunc(l / r) # left / right, // is math.floor, use trunc
                
                integer_stack.append(temp)
                    
        return integer_stack[0]