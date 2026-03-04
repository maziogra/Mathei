# Autore: Shahid

import sympy as sp
from Sign.findNearestPeriod import findNearestPeriod
from Sign.findCriticalPoints import findCriticalPoints
from Sign.findSolution import findSolution

def analizer(expr, x, flag = False):
    res = []

    if expr.is_polynomial(x):
        for i in findCriticalPoints(expr, x):
            res.append(i)
        return res
    
    # Mul, Add ecc. con i metodi di sympy
    if getattr(expr, 'is_Mul', False):
        for arg in expr.args:
            if arg.has(sp.sin, sp.cos, sp.tan):
                res.append(findNearestPeriod(arg, x, []))
            else:
                for i in findCriticalPoints(arg, x):
                    res.append(i)
    elif getattr(expr, 'is_Add', False):
        
        for i in findSolution(expr, x):
            print("Nel add: ", i)
            res.append(i)
        return res
    else:
        if expr.has(sp.sin, sp.cos, sp.tan):
            res.append(findNearestPeriod(expr, x, []))
        else:
            for i in findCriticalPoints(expr, x, flag):
                res.append(i)
    print("----------------------", res)
    return res
