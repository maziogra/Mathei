# Autore: Shahid

import sympy as sp
from Sign.addDomainPoints import addDomainPoints

def findSolution(f, x):
    a = float(0)
    b = float(2 * sp.pi)

    guesses = [a + i*(b-a)/50 for i in range(-50,50)]
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
    for i in range(len(solutions)):
        val = solutions[i]
        if val == 3.14159265359:
            solutions[i] = sp.pi
        elif val == 6.28318530718:
            solutions[i] = 2 * sp.pi
        elif val == -3.14159265359:
            solutions[i] = -sp.pi
        elif val == -6.28318530718:
            solutions[i] = -2 * sp.pi
        else:
            if abs(val - round(val)) < 1e-6:
                solutions[i] = int(round(val))
            else:
                solutions[i] = val
    solutions = sorted(solutions)
    domain = sp.calculus.util.continuous_domain(f, x, domain=sp.Reals)
    addDomainPoints(domain, solutions)
    print("Nel pol: ", solutions)
    return solutions