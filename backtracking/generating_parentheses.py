class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Given n pairs of parentheses, generate all combinations of well-formed parentheses.

        Args:
            n(int): number of set of parentheses
        
        Return:
            list(str): parenthesis combination

        Time Complexity: O(2^n)
        Space Complexity: O(2^n)

        Tricks: imagine a recursion tree
        """
        # Backtracking
        # def backtrack(s, open_count, close_count):
        #     if len(s) == n*2:
        #         res.append(s) 
        #     if len(s) < n*2:
        #         if open_count < n:
        #             backtrack(s + '(', open_count+1, close_count)
        #         if close_count < open_count:
        #             backtrack(s + ')', open_count, close_count+1)

        # res = []
        # backtrack('', 0, 0)
        # return res

        # Dynamic Programming
        dp = [[] for _ in range(n+1)]
        dp[0] = [""]

        # use (n=1,n=1; n=0,n=2; n=2,n=0) to constructe n=3 
        for k in range(n+1): # use k pair parenthesis for combinations (3 pair)
            for i in range(k): # look previous ith valid combinations where i=0...k (0, 1, 2 pair result)
                for inside in dp[i]: # split the previous result to two parts (res[0] & res[2], res[1] & res[1])
                    for outside in dp[k-i-1]:
                        dp[k].append('(' + inside + ')' + outside)

        return dp[-1]