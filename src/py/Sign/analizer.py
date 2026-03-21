# Autore: Shahid

import sympy as sp
from Sign.findCriticalPoints import findCriticalPoints
from Sign.findSolution import findSolution

def analizer(expr, x):
    res = []

    if expr.is_polynomial(x):
        for i in findCriticalPoints(expr, x):
            res.append(i)
        return res
    
    # Mul, Add ecc. con i metodi di sympy
    if getattr(expr, 'is_Mul', False):
        for arg in expr.args:
            for i in findCriticalPoints(arg, x):
                res.append(i)    
    elif getattr(expr, 'is_Add', False): 
        for i in findSolution(expr, x):
            res.append(i)
        return res
    else:
        for i in findCriticalPoints(expr, x):
            res.append(i)
    return res
