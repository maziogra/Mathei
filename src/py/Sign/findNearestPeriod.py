# Autore: Shahid
# Refactoring: maziogra

import sympy as sp
from Sign.addDomainPoints import addDomainPoints
from Utils.findPeriod import findPeriod
from Domain.domain import domain as findDomain

def findNearestPeriod(f, x):
    period = findPeriod(f, x)
    d = findDomain(f, x)

    if period is None:
        return []
    
    a = 0
    b = period

    while a not in d or b not in d:
        a = b
        b += period

    print("-------------------", a, "   ", b)
    domain = sp.calculus.util.continuous_domain(f, x, domain=sp.Interval(a, b, left_open=False, right_open=False))
    zeros = sp.solveset(f, x, domain=sp.Interval(a, b, left_open=False, right_open=False))

    if zeros == sp.EmptySet:
        zeros = []
    else:
        zeros = list(zeros)
    addDomainPoints(domain, zeros)
    zeros = sorted(zeros)
    print("######################",zeros)
    return zeros
