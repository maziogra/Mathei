# Autore: Khadija

import sympy as sp
from core.Utils.findPeriod import findPeriod
from core.Utils.findNearestPeriod import findNearestPeriod

def intersections(f):
    x=sp.symbols("x")
    d=sp.S.Reals

    if isGoniometric(f):
        a, b = findNearestPeriod(f, x)
        d = sp.Interval(a, b)
    #int con asse x y=0
    intersectionsxy=[]
    try:
        zeri = sp.solveset(f, x, d)
        print(zeri)
        if isinstance(zeri, sp.FiniteSet):
            for zero in zeri:
                intersectionsxy.append((zero,0))
    except Exception as excep:
        intersectionsxy.append("errore asse x")
    #int con asse y x=0 
    try:
        perxZero=f.subs(x, 0).evalf()
        if perxZero.is_real and perxZero.is_finite:
            if (0, perxZero) not in intersectionsxy:
                intersectionsxy.append((0,perxZero))
    except Exception as excep:
        intersectionsxy.append("errore asse y ")

    #risultati stmpa
    print("punti di intersezione con gli assi ")
    for point in intersectionsxy:
        print(point)
    return(intersectionsxy)
# controllo ha gonio
def isGoniometric(f):
    goniometric = [sp.sin, sp.cos, sp.tan, sp.cot, sp.sec, sp.csc]
    return any(f.has(func) for func in goniometric)
