# Autore: maziogra
# Refactoring: Shahid

import sympy as sp
from Sign.addDomainPoints import addDomainPoints
from Sign.test import test

def findCriticalPoints(f, x):
    # trovo zeri e dominio da cui estrarro i punti critici
    points = sp.solveset(f, x, domain=sp.S.Reals)
    domain = sp.calculus.util.continuous_domain(f, x, sp.S.Reals)
    
    # se i punti sono finiti vuol dire che non è una goniometrica
    # da rivedere, forse ci sono altri casi
    if isinstance(points, sp.FiniteSet) or points == sp.EmptySet:
        points = list(points)

    # metto nell'insieme dei punti anche i punti in cui la funz non esiste
    addDomainPoints(domain, points)
    
    signs = []
    signs, points = test(points, signs, f, x)
    return points, signs
