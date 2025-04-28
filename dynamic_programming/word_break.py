from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Check if string s can be segmented into wordDict words

        Args:
            s: string
            wordDict; dictionary of available word for form s

        Return:
            bool: return True if s can be segmented into dict word

        Time Complexity: O()
        Space Complexity: O(n)

        Trick: Dynamic Programming, coin problem, dict is the coin

        Memo optimal word segmentation up to i
            dp[i] = word index in dict, where 0 <= 0 < len(s)
            dp[i] = if a valid segmenetation is present for s = 0...i+1
        Backtrack
        String comparison

        start should be exclusive of the current word 
        for leetcode, when we match leet, we check dp[0]=true, whereas dp[1]:l, dp[2]:e, dp
        """
        dp = [True] + [False] * len(s)

        for i in range(1, len(s)+1):
            for w in wordDict:
                start = i - len(w)
                # find valid match: valid length + previous valid + word match
                if start>=0 and dp[start] and s[start:i] == w:
                    dp[i] = True
                    break

        return dp[-1] 

        # Useful for the case if we want to know which words are used
        # for i in range(len(s)):
        #     for j in range(len(wordDict)):
        #         word_length = len(wordDict[j]) # obtain word
        #         if word_length > i+1: continue  # skip the word case

        #         # print(i, j, i-word_length+1, s[i-word_length+1:i+1], wordDict[j], dp)
        #         # check if it does match and previous characters are valid
        #         if dp[i-word_length+1] is not None and s[i-word_length+1:i+1] == wordDict[j]:
        #             dp[i+1] = j
        
        # # backtrack: check valid segmentation
        # j = len(s)
        # while j > 0 and dp[j] is not None:
        #     word = wordDict[dp[j]]
        #     j -= len(word)
        
        # print(dp)
        # # valid if string can be perfectly segmented with no character left
        # return j == 0