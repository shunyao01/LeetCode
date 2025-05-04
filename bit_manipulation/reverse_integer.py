class Solution:
    def reverse(self, x: int) -> int:
        """
        Reverse 32 bit integer

        The range of a signed 32-bit integer is:
            -2,147,483,648 to 2,147,483,647

        Time Complexity: O(log₁₀x) — Each digit is processed once
        Space Complexity: O(1) — Constant extra space used

        Args:
            x (int): The integer to be reversed

        Returns:
            int: The reversed integer, or 0 if it overflows
        """
        res = 0
        sign = 1 if x>0 else -1
        x = abs(x)

        max_n = 2 ** 31 - 1
        min_n = - 2 ** 31

        # from right to left
        while x != 0:

            digit = x % 10
            x = x // 10

            if sign == 1:
                if res > max_n // 10 or res == max_n // 10 and digit > 7: # max_n % 10
                    return 0
            else:
                if res > max_n // 10 or res == max_n // 10 and digit > 8: # abs(min_n % -10)
                    return 0

            res = res * 10 + digit

        return sign * res