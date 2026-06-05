# Autore: maziogra
# Refactoring: Shahid

import sympy as sp
from core.Sign.addDomainPoints import addDomainPoints
from core.Utils.findNearestPeriod import findNearestPeriod
from core.Utils.isGonio import isGonio

def findCriticalPoints(f, x, flag = False):
    a = -sp.oo
    b = sp.oo

    f = sp.expand_trig(f)
    if isGonio(f, x):
        result = findNearestPeriod(f, x)
        if result == []:
            return result, True
        else:
            a, b = result

    # trovo zeri e dominio da cui estraggo i punti critici
    points = sp.solveset(f, x, domain=sp.Interval(a, b, left_open=False, right_open=False))
    if points == sp.EmptySet:
        points = []
    elif isinstance(points, sp.Interval):
        points = [points.start, points.end]
    elif isinstance(points, sp.ConditionSet) or points.has(sp.ConditionSet):
        return points, True
    else:
        points = list(points)
    try:
        domain = sp.calculus.util.continuous_domain(f, x, domain=sp.Interval(a, b, left_open=False, right_open=False))
    except Exception:
        return [], True

    if isGonio(f, x):
        if a is not -sp.oo:
            points.append(a)
        if b is not sp.oo:
            points.append(b)

    # metto nell'insieme dei punti anche i punti in cui la funz non esiste
    addDomainPoints(domain, points)
    
    return points, False
