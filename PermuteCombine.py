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
    if n == r: return  1.0 * Factorial(n,appr)
    if r == 0: return 1
    return 1.0 * Factorial(n,appr) / Factorial(n-r,appr)

def CountCombinations(n, r, appr=True):
    if n == r: return 1
    if r == 0: return 1
    return (1.0 * Factorial(n,appr)) / (Factorial(r,appr) * Factorial(n-r,appr))

"""
TEST:
    There are ~830PNs in total (with 80-130 reliable PNs), and ~50000KCs.
     & the probility that a PN and KC is connected is quite close to 0.5
"""

'''
PN_num = 80 # 830
KC_num = 5000 # 50000
PN_feedin_num = PN_num/2

def relyPN_to_KC(x=PN_feedin_num, k=10, rely=10):
    """compute the probility that all reliable PNs are connected to a given KC:
    >>> x is total pick up PN number,
    >>> k is picked up reliable PN number,
    >>> rely is total reliable PN number, 80-130 for 830 PNs
    """
    return CountCombinations(rely, k) * CountCombinations(PN_num-rely, x-k) / CountCombinations(PN_num, x)

rely = 8
l1=[]
print "\nThere are", rely, "reliable PNs:"
for k in range(0, rely+1, 1):
    ttt=relyPN_to_KC(PN_feedin_num, k, rely)
    print k, ttt
    l1.append(ttt)

rely = 9
l2=[]
print "\nThere are", rely, "reliable PNs:"
for k in range(0, rely+1, 1):
    ttt=relyPN_to_KC(PN_feedin_num, k, rely)
    print k, ttt
    l2.append(ttt)

rely = 10
l3=[]
print "\nThere are", rely, "reliable PNs:"
for k in range(0, rely+1, 1):
    ttt=relyPN_to_KC(PN_feedin_num, k, rely)
    print k, ttt
    l3.append(ttt)

rely = 11
l4=[]
print "\nThere are", rely, "reliable PNs:"
for k in range(0, rely+1, 1):
    ttt=relyPN_to_KC(PN_feedin_num, k, rely)
    print k, ttt
    l4.append(ttt)

rely = 12
l5=[]
print "\nThere are", rely, "reliable PNs:"
for k in range(0, rely+1, 1):
    ttt=relyPN_to_KC(PN_feedin_num, k, rely)
    print k, ttt
    l5.append(ttt)

rely = 13
l6=[]
print "\nThere are", rely, "reliable PNs:"
for k in range(0, rely+1, 1):
    ttt=relyPN_to_KC(PN_feedin_num, k, rely)
    print k, ttt
    l6.append(ttt)

figure()
plot(l1)
plot(l2)
plot(l3)
plot(l4)
plot(l5)
plot(l6)

tttt=[l1[-1], l2[-1], l3[-1], l4[-1], l5[-1], l6[-1]]
figure()
plot(tttt)  '''
