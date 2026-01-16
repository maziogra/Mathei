import sympy as sp
from Sign.trovaPuntiCritici import trovaPuntiCritici
from Sign.addInfinite import addInfinite
from Sign.test import test
from Sign.analizer import analizer
from Sign.findSolution import findSoluntion

def createSign(f, x):
    signs = []
    interlvals = []
    functionDomain = sp.calculus.util.continuous_domain(f, x, sp.S.Reals)
     
    # prova a interpretarla come polinomio in x 
    try:
        p = sp.Poly(f, x)
        grado = p.degree()
        if grado == 1 or grado == 2:
            signs.append(trovaPuntiCritici(f, x))
    except:
        pass

    signs += analizer(f, x)

    print("Final signs:")
    print(signs)
    
    for element in signs:
        for interval in element[0]:
            interlvals.append(interval)

    
    print("Combined intervals:", interlvals)
    interlvals = sorted(interlvals)
    domain = sp.Intersection(sp.Interval(interlvals[0], interlvals[-1], left_open=False, right_open=False), functionDomain)
    sol = sp.solveset(f, x, domain=domain)
    
    if sol != sp.EmptySet:
        if isinstance(sol, sp.ConditionSet):
            sol = findSoluntion(f, x)
            interlvals += sorted(sol)
        else:
            sol = list(sol)
            interlvals += sorted(sol)
        print("solveset: ", sol)

    interlvals = list(set(interlvals))
    interlvals = sorted(interlvals)
    print("Combined intervals:", interlvals)
    
    # Aggiunge -oo e +oo agli intervalli se non sono presenti pi all'inizio e alla fine
    addInfinite(interlvals)
    
    finalsigns = []
    finalsigns, interlvals = test(interlvals, finalsigns, f, x)
    for i in range(len(finalsigns)):
            print(f"Intervallo {interlvals[i]} -> {interlvals[i+1]}: segno {finalsigns[i]}")
    print("Continua poi come la funzione goniometrica singola...")