from typing import List

class Solution:
    """
    Encode list of strings to a single string and decode back to original strings

    Use '/' as seperator
    """

    def encode(self, strs: List[str]) -> str:
        i = 0
        while i < len(strs):
            s = strs[i]
            l = len(s)
            strs.insert(i, str(l) + '#')
            i += 2

        # print(strs)
        return ''.join(strs) 


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            print(s, res, i)
            # Read length
            l = 0
            while s[i] != '#': # find length, stop after #
                l = l * 10 + int(s[i])
                i += 1
            
            # Read string
            i += 1
            res.append(s[i:i+l])
            i += l

        return res