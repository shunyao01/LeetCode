class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Check if ransomnote can be constructed using letter from magazine

        Args:
            ransomNote: string that is a potential subset of magazine
            magazine: string that need to "cover" ransomNote

        Return:
            Boolean, if it can be constructed

        Time Complexity: O(m+n)
        Space Complexity: O(1)

        Lowercase letter: integer array size 26
        """
        arr = [0] * 26

        # Record frequency of each letter in magazine
        for c in magazine:
            arr[ord(c)-ord("a")] += 1

        # Check if all letters are used up
        for c in ransomNote:
            arr[ord(c)-ord("a")] -= 1

        # Check if integer array values > 0
        return all([f >= 0 for f in arr])