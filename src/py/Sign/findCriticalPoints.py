# Autore: maziogra
# Refactoring: Shahid

import sympy as sp
from Sign.addDomainPoints import addDomainPoints
from Sign.test import test

def findCriticalPoints(f, x, flag = False):
    # trovo zeri e dominio da cui estrarro i punti critici
    points = []
    if not flag:
        points = sp.solveset(f, x, domain=sp.S.Reals)
        # se i punti sono finiti vuol dire che non è una goniometrica
        # da rivedere, forse ci sono altri casi
        if isinstance(points, sp.FiniteSet) or points == sp.EmptySet:
            points = list(points)
    domain = sp.calculus.util.continuous_domain(f, x, sp.S.Reals)
    

    # metto nell'insieme dei punti anche i punti in cui la funz non esiste
    addDomainPoints(domain, points)
    return points
