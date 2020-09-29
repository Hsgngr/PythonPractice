"""
Created by  Ege of the House Hoşgüngör, the First of His Name  at 12:52 29.09.2020
"""
import math
import os
import random
import re
import sys

example_score = [
    10, 5, 20, 20, 4, 5, 2, 25, 1]


# Complete the breakingRecords function below.
def breakingRecords(scores):
    n = len(scores)
    min_score = scores[0]
    max_score = scores[0]
    min_counter = 0
    max_counter = 0
    max_min_score = [max_counter, min_counter]

    for i in range(1, n):
        if scores[i] < min_score:
            min_score = scores[i]
            min_counter += 1
        elif scores[i] > max_score:
            max_score = scores[i]
            max_counter += 1

    max_min_score = [max_counter, min_counter]

    return max_min_score



print(breakingRecords(example_score))
