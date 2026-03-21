# Autore: maziogra
# Refactoring: Shahid

import sympy as sp
from Sign.addDomainPoints import addDomainPoints
from Utils.findNearestPeriod import findNearestPeriod
from Sign.test import test

def findCriticalPoints(f, x, flag = False):
    a = -sp.oo
    b = sp.oo

    f = sp.expand_trig(f)
    if f.has(sp.cos, sp.sin, sp.tan):
        a, b = findNearestPeriod(f, x)


    # trovo zeri e dominio da cui estrarro i punti critici
    points = sp.solveset(f, x, domain=sp.Interval(a, b, left_open=False, right_open=False))
    if points == sp.EmptySet:
        points = []
    elif isinstance(points, sp.Interval):
        points = [points.start, points.end]
    else:
        print("###########################", points)
        points = list(points)
    domain = sp.calculus.util.continuous_domain(f, x, domain=sp.Interval(a, b, left_open=False, right_open=False))
    

    # metto nell'insieme dei punti anche i punti in cui la funz non esiste
    addDomainPoints(domain, points)
    return points
