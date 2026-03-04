# Autore: Shahid

import sympy as sp
from Sign.findCriticalPoints import findCriticalPoints
from Sign.addInfinite import addInfinite
from Sign.test import test
from Sign.analizer import analizer
from Sign.findSolution import findSolution

def createSign(f, x):
    intervals = []
    functionDomain = sp.calculus.util.continuous_domain(f, x, sp.S.Reals)

    signs = analizer(f, x)

    print("Final signs:")
    print(signs)
    
    
    '''print("Combined intervals:", intervals)
    intervals = sorted(intervals)
    domain = sp.Intersection(sp.Interval(intervals[0], intervals[-1], left_open=False, right_open=False), functionDomain)
    sol = sp.solveset(f, x, domain=domain)
    
    if sol != sp.EmptySet:
        if isinstance(sol, sp.ConditionSet):
            sol = findSolution(f, x)
            intervals += sorted(sol)
        else:
            sol = list(sol)
            intervals += sorted(sol)
        print("solveset: ", sol)

    intervals = list(set(intervals))
    intervals = sorted(intervals)
    print("Combined intervals:", intervals)
    
    # Aggiunge -oo e +oo agli intervalli se non sono presenti pi all'inizio e alla fine
    addInfinite(intervals)
    
    finalsigns = []
    finalsigns, intervals = test(intervals, finalsigns, f, x)
    for i in range(len(finalsigns)):
            print(f"Intervallo {intervals[i]} -> {intervals[i+1]}: segno {finalsigns[i]}")
    print("Continua poi come la funzione goniometrica singola...")'''