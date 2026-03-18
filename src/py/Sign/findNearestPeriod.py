# Autore: Shahid

import sympy as sp
from Sign.addDomainPoints import addDomainPoints
from Utils.findPeriod import findPeriod

def findNearestPeriod(f, x):
    max_period = -sp.oo
    min_period = sp.oo
    
    # calculate the period of the goniometric function until the nearest extremes
    left = -1
    right = 1
    period = findPeriod(f, x)

    if period is None:
        return []
    
    leftExtreme = -float(period)
    rightExtreme = float(period)
    
    while leftExtreme > float(min_period):
        leftExtreme -= float(period)
        left -= 1
    while rightExtreme < float(max_period):
        rightExtreme += float(period)
        right += 1

    leftExtreme = left * period
    rightExtreme = right * period

    domain = sp.calculus.util.continuous_domain(f, x, domain=sp.Interval(leftExtreme, rightExtreme, left_open=False, right_open=False))
    zeros = sp.solveset(f, x, domain=sp.Interval(leftExtreme, rightExtreme, left_open=False, right_open=False))
    if zeros == sp.EmptySet:
        zeros = []
    else:
        zeros = list(zeros)
    addDomainPoints(domain, zeros)
    zeros = sorted(zeros)
    return zeros