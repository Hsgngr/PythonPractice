"""
Created by  Ege of the House Hoşgüngör, the First of His Name  at 19:22 1.10.2020
"""
import math
import os
import random
import re
import sys
#https://www.hackerrank.com/challenges/the-birthday-bar/problem

# Complete the birthday function below.
def birthday(s, d, m):
    counter = 0

    for i in range(len(s) - m + 1):
        print(s[i:i + m])
        if (sum(s[i:i + m])) == d:
            counter += 1
    return counter


s = [1, 2, 1, 3, 2]
d = 3
m = 2

result = birthday(s, d, m)
print(result)
