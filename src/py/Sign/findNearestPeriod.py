# Autore: Shahid

import sympy as sp
from Sign.test import test
from Sign.addDomainPoints import addDomainPoints
from Utils.findPeriod import findPeriod

def findNearestPeriod(f, x, signs):
    periods = []
    
    # Collect existing periods from signs
    for element in signs:
        periods.append(element[0])

    periods = sorted(periods)
    max_period = -sp.oo
    min_period = sp.oo
    # Find the extremes of the existing periods
    for element in periods:
        for number in element:
            if number > float(max_period):
                max_period = number
            if number < float(min_period):
                min_period = number
    
    # calculate the period of the goniometric function until the nearest extremes
    left = -1
    right = 1
    period = findPeriod(f, x)
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
        
    print("Searching zeros in interval:", (leftExtreme, rightExtreme))
    domain = sp.calculus.util.continuous_domain(f, x, domain=sp.Interval(leftExtreme, rightExtreme, left_open=False, right_open=False))
    print("Domain in nearest period: ", domain)
    zeros = sp.solveset(f, x, domain=sp.Interval(leftExtreme, rightExtreme, left_open=False, right_open=False))
    if zeros == sp.EmptySet:
        zeros = []
    else:
        zeros = list(zeros)
    addDomainPoints(domain, zeros)
    zeros = sorted(zeros)
    signs2 = []
    signs2, zeros = test(zeros, signs2, f, x)

    return (zeros, signs2)