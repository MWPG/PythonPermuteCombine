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

from decimal import *
getcontext().prec = 10

def StirlingFactorial(n):
    "Stirling's approximation for factorials (NOT used for overflow issue)"
    return Decimal((n/e)**n) * Decimal(sqrt(2*pi*n))

def Factorial(n):
    return Decimal(math.factorial(n))

def CountPermutations(n, r):
    if n == r: return Decimal(1.0) * Factorial(n)
    if r == 0: return Decimal(1.0)
    return Decimal(1.0) * Factorial(n) / Factorial(n-r)

def CountCombinations(n, r):
    if n == r: return Decimal(1.0)
    if r == 0: return Decimal(1.0)
    return (Decimal(1.0) * Factorial(n)) / (Factorial(r) * Factorial(n-r))

"""
TEST:
    There are ~830PNs in total (with 80-130 reliable PNs), and ~50000KCs.
     & the probility that a PN and KC is connected is quite close to 0.5
"""

PN_num = 830
KC_num = 50000
PN_feedin_num = PN_num/2

def relyPN_to_KC(x=PN_feedin_num, k=80, rely=100):
    """compute the probility that all reliable PNs are connected to a given KC:
    >>> x is total pick up PN number,
    >>> k is picked up reliable PN number,
    >>> rely is total reliable PN number, 80-130 for 830 PNs
    """
    return CountCombinations(rely, k) * CountCombinations(PN_num-rely, x-k) / CountCombinations(PN_num, x)

"""
suppose there are 800 reliable PNs in total, and we randomly select PN_feedin_num PNs to connect to a given KC,
then, how many reliable PNs would be in the selected PN set?
"""
rely = 80
l1 = []
print "\nThere are", rely, "reliable PNs:"
for k in range(0, rely+1, 10):
    ttt = relyPN_to_KC(PN_feedin_num, k, rely)
    print k, ttt
    l1.append(ttt)

rely = 90
l2 = []
print "\nThere are", rely, "reliable PNs:"
for k in range(0, rely+1, 10):
    ttt = relyPN_to_KC(PN_feedin_num, k, rely)
    print k, ttt
    l2.append(ttt)

rely = 100
l3 = []
print "\nThere are", rely, "reliable PNs:"
for k in range(0, rely+1, 10):
    ttt = relyPN_to_KC(PN_feedin_num, k, rely)
    print k, ttt
    l3.append(ttt)

rely = 110
l4 = []
print "\nThere are", rely, "reliable PNs:"
for k in range(0, rely+1, 10):
    ttt = relyPN_to_KC(PN_feedin_num, k, rely)
    print k, ttt
    l4.append(ttt)

rely = 120
l5 = []
print "\nThere are", rely, "reliable PNs:"
for k in range(0, rely+1, 10):
    ttt = relyPN_to_KC(PN_feedin_num, k, rely)
    print k, ttt
    l5.append(ttt)

rely = 130
l6 = []
print "\nThere are", rely, "reliable PNs:"
for k in range(0, rely+1, 10):
    ttt = relyPN_to_KC(PN_feedin_num, k, rely)
    print k, ttt
    l6.append(ttt)

figure()
plot(l1)
plot(l2)
plot(l3)
plot(l4)
plot(l5)
plot(l6)

def PS(x, lamda):
    "Poisson distribution density with parameter lamda at the point x"
    return math.exp(-lamda)*(lamda**x)/math.factorial(x)

"Poisson distribution can be used to approxmiate binary distribution"
for i in range(100):
    print i, PS(i, KC_num*0.00001)
#                           \--- this probablity is printed above,
#                                choose the correct one， and note
#                                range(100) may also need to be fixed
