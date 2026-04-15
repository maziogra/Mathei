# Autore: maziogra
# Refactoring: Shahid

import sympy as sp
from core.Sign.addDomainPoints import addDomainPoints
from core.Utils.findNearestPeriod import findNearestPeriod
from core.Sign.test import test

def findCriticalPoints(f, x, flag = False):
    a = -sp.oo
    b = sp.oo

    f = sp.expand_trig(f)
    if f.has(sp.cos, sp.sin, sp.tan):
        result = findNearestPeriod(f, x)
        if result == []:
            return result, True
        else:
            a, b = result

    # trovo zeri e dominio da cui estrarro i punti critici
    points = sp.solveset(f, x, domain=sp.Interval(a, b, left_open=False, right_open=False))
    if points == sp.EmptySet:
        points = []
    elif isinstance(points, sp.Interval):
        points = [points.start, points.end]
    else:
        points = list(points)
    domain = sp.calculus.util.continuous_domain(f, x, domain=sp.Interval(a, b, left_open=False, right_open=False))
    points.append(a)
    points.append(b)

    # metto nell'insieme dei punti anche i punti in cui la funz non esiste
    addDomainPoints(domain, points)
    
    return points, False
