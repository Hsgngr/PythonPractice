# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 13:59:55 2020

@author: Ege

BRIEF TOUR OF STANDARD LIBRARY: https://docs.python.org/3/tutorial/stdlib.html

"""

import os
dir(os)
help(os)
#Get directory
os.getcwd()
#Change directory
os.chdir('E:\\Ege\\Works\\MachineLearningProjects\\MachineLearning\\Handson_ML\\')

#Run the commmand mkdir in the system shell (Create new directory)
os.system('mkdir mk')
#Delete the mk directory
os.system('rmdir mk')

#The glob module provides a function for making file lists from directory wildcard searches:
import glob
glob.glob('*.py')

'''
Out[175]: ['understanding_data.py', '_cleaning.py']
'''

#Command Line Arguments
import sys
print(sys.argv)

import argparse


#Mathematics
import math
import random
import statistics

#Internet Access
from urllib.request import urlopen
with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl') as response:
    for line in response:
        line = line.decode('utf-8')  # Decoding the binary data to text.
        if 'EST' in line or 'EDT' in line:  # look for Eastern Time
            print(line)
            
#Dates and Times
from datetime import date
now = date.today()
print(now)

#Data Compression
import zlib
s = b'witch which has which witches wrist watch'
len(s)

t = zlib.compress(s)
len(t)
zlib.decompress(t)
zlib.crc32(s)

#Performance Measurement
from timeit import Timer
Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()

#Quality Control
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()   # automatically validate the embedded tests

#The unittest module is not as effortless as the doctest module,
# but it allows a more comprehensive set of tests to be maintained in a separate file:
    
import unittest

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

unittest.main()  # Calling from the command line invokes all tests