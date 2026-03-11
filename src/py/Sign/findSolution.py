# Autore: Shahid

import sympy as sp
from Sign.addDomainPoints import addDomainPoints
from Utils.simplifyPi import simplifyPi

def findSolution(f, x):
    a = -float(2 * sp.pi)
    b = float(2 * sp.pi)

    guesses = [a + i*(b)/50 for i in range(0,50)]
    solutions = set()
    for g in guesses:
        try:
            r = sp.nsolve(f, g, tol=1e-14, maxsteps=50)
            rv = float(r)
            if a <= rv <= b:
                solutions.add(round(rv, 12))
        except Exception:
            pass

    solutions = list(solutions)
    solutions = [simplifyPi(v) for v in solutions]
    solutions = sorted(solutions)
    domain = sp.calculus.util.continuous_domain(f, x, domain=sp.Reals)
    addDomainPoints(domain, solutions)
    return solutions