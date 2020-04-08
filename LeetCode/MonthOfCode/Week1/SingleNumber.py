# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3283/
from typing import List

# Basic Solution with a set
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         seen_nums = set()
#         for num in nums:
#             if num in seen_nums:
#                 seen_nums.remove(num)
#             else:
#                 seen_nums.add(num)
#         return seen_nums.pop()

# Fastest Solution with XOR operator
# XOR is communative and A ^ A = 0
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        val = 0
        for num in nums:
            val ^= num
        return val
