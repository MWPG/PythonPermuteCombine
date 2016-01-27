#  !/usr/bin/env python
#  -*- coding:utf-8 -*-

#  ==============================================
#  ·
#  · Author: Mogei Wang
#  ·
#  · MogeiWang@GMail.com
#  ·
#  · COPYRIGHT 2016
#  ·
#  ==============================================

"""
>>> import itertools
>>> for i in itertools.product('ABCD', repeat = 2):
...     print i,
... 
('A', 'A') ('A', 'B') ('A', 'C') ('A', 'D') ('B', 'A') ('B', 'B') ('B', 'C') ('B', 'D') ('C', 'A') ('C', 'B') ('C', 'C') ('C', 'D') ('D', 'A') ('D', 'B') ('D', 'C') ('D', 'D')
>>> for i in itertools.permutations('ABCD', 2):
...     print i,
... 
('A', 'B') ('A', 'C') ('A', 'D') ('B', 'A') ('B', 'C') ('B', 'D') ('C', 'A') ('C', 'B') ('C', 'D') ('D', 'A') ('D', 'B') ('D', 'C')
>>> for i in itertools.combinations('ABCD', 2):
...     print i,
... 
('A', 'B') ('A', 'C') ('A', 'D') ('B', 'C') ('B', 'D') ('C', 'D')
>>> for i in itertools.combinations_with_replacement('ABCD', 2):
...     print i,
... 
('A', 'A') ('A', 'B') ('A', 'C') ('A', 'D') ('B', 'B') ('B', 'C') ('B', 'D') ('C', 'C') ('C', 'D') ('D', 'D')
"""

"""
https://docs.python.org/2/library/itertools.html
"""

def StirlingFactorial(n):
    "Stirling's approximation for factorials"
    return (n/e)**n * sqrt(2*pi*n)

def Factorial(n, appr=True):
    if appr:
        return StirlingFactorial(n)
    else:
        return math.factorial(n)

def CountPermutations(n, r, appr=True):
    return 1.0 * Factorial(n,appr) / Factorial(n-r, appr)

def CountCombinations(n, r, appr=True):
    return (1.0 * Factorial(n,appr)) / (Factorial(r,appr) * Factorial(n-r,appr))
