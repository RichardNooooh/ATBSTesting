# https://leetcode.com/explore/other/card/30-day-leetcoding-challenge/528/week-1/3284/
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        seen.add(n)
        while True:
            digits = str(n)
            n = 0
            for digit in digits:
                n += int(digit) ** 2
            if n == 1:
                return True
            elif n in seen:
                return False
