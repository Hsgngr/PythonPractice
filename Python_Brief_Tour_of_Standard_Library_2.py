# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 18:49:49 2020

@author: Ege
"""

#11 Output Formatting
import reprlib
X = reprlib.repr(set('supercalifragilisticexpialidocious'))


import pprint
x = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta','yellow'], 'blue']]]

pprint.pprint(x, width=30)


import textwrap

doc = """The wrap() method is just like fill() except that it returns
... a list of strings instead of one big string with newlines to separate
... the wrapped lines."""

print(textwrap.fill(doc, width=40))

'''
The locale module accesses a database of culture specific data formats.
The grouping attribute of locale’s format function provides a 
direct way of formatting numbers with group separators:
'''
import locale
locale.setlocale(locale.LC_ALL, 'English_United States.1252')

conv = locale.localeconv()

x = 1234567.8
locale.format("%d", x, grouping=True)

locale.format_string("%s%.*f", (conv['currency_symbol'], conv['frac_digits'], x), grouping=True)
