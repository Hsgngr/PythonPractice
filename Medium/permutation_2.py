"""
Created by  Ege of the House Hoşgüngör, the First of His Name  at 19:56 12.11.2020

https://leetcode.com/problems/permutations-ii/ LeetCode Nov 12

A bit cheated by using itertools, here is the solution:
https://leetcode.com/problems/permutations-ii/solution/

"""
import itertools


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        output_set = set()
        comb = itertools.permutations(nums, len(nums))
        for sequence in comb:
            output_set.add(sequence)

        return output_set
