# Autore: Shahid
# Refactoring: maziogra

import sympy as sp
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
    
    return a, b

