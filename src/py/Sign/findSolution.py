# Autore: Shahid

import sympy as sp
from Sign.addDomainPoints import addDomainPoints
from Utils.simplifyPi import simplifyPi
from Utils.findNearestPeriod import findNearestPeriod

def findSolution(f, x):
    a = -float(100)
    b = float(100)

    f_exp = sp.expand_trig(f)
    if f_exp.has(sp.cos, sp.sin, sp.tan):
        a, b = findNearestPeriod(f_exp, x)
        a = float(a)
        b = float(b)
        print(a, b)

    d = sp.calculus.util.continuous_domain(f, x, domain=sp.Interval(a, b, left_open=False, right_open=False))

    guesses = [i/3 for i in range(-300,300)]
    solutions = set()
    for i in range(0, len(guesses)-1):

        in_domain = d.contains(guesses[i]) and d.contains(guesses[i+1])

        if not in_domain:
            continue

        eq_sign = sp.sign(f.subs(x, guesses[i]).evalf()) == sp.sign(f.subs(x, guesses[i+1]).evalf())
        
        if eq_sign:
            continue

        try:
            r = sp.nsolve(f, guesses[i], tol=1e-14)
            rv = float(r)
            if a <= rv <= b:
                solutions.add(round(rv, 12))
        except Exception:
            pass

    solutions = list(solutions)
    solutions = [simplifyPi(v) for v in solutions]
    solutions = sorted(solutions)
    addDomainPoints(d, solutions)
    
    return solutions