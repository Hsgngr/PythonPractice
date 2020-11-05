# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 21:43:17 2020

@author: Ege

November Coding Challenge Day 5

https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/564/week-1-november-1st-november-7th/3520/

"""

class Solution(object):
    def minCostToMoveChips(self, position):
        """
        :type position: List[int]
        :rtype: int
        """
        n= len(position)
        odds= 0
        evens= 0
        
        for i in range(n):
            if position[i] % 2 == 0:
                evens += 1
            else: odds +=1
        print(evens)
        print(odds)
        
        return min(evens,odds)
        