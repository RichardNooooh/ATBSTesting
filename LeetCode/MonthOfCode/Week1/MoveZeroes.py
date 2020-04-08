# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3286/
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # I think this is a pretty slow solution
        i = len(nums) - 1
        last_zero = i
        for num in nums[::-1]:
            if num == 0:
                temp = nums[i]
                nums[last_zero] = 0
                nums[i] =
                last_zero -= 1

