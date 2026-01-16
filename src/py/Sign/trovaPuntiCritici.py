import sympy as sp
from Sign.addDomainPoints import addDomainPoints
from Sign.test import test

def trovaPuntiCritici(f, x):
    # trovo zeri e dominio da cui estrarro i punti critici
    punti = sp.solveset(f, x, domain=sp.S.Reals)
    dominio = sp.calculus.util.continuous_domain(f, x, sp.S.Reals)
    
    # se i punti sono finiti vuol dire che non è una goniometrica
    # da rivedere, forse ci sono altri casi
    if isinstance(punti, sp.FiniteSet) or punti == sp.EmptySet:
        punti = list(punti)
    
    
    # metto nell'insieme dei punti anche i punti in cui la funz non esiste
    addDomainPoints(dominio, punti)
    
    signs = []
    signs, punti = test(punti, signs, f, x)
    return punti, signs
