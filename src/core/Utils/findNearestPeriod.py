# Autore: Shahid
# Refactoring: maziogra

import sympy as sp
from core.Utils.findPeriod import findPeriod

def findNearestPeriod(f, x):
    period = findPeriod(f, x)

    if period is None:
        return []

    a = 0
    b = period
    
    return a, b