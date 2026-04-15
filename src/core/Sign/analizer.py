# Autore: Shahid

import sympy as sp
from core.Sign.findCriticalPoints import findCriticalPoints
from core.Sign.findSolution import findSolution

def analizer(expr, x):
    res = []
    warning = False

    if expr.is_polynomial(x):
        points, warning = findCriticalPoints(expr, x)
        for i in points:
            res.append(i)
        return res, warning
    
    # Mul, Add ecc. con i metodi di sympy
    if getattr(expr, 'is_Mul', False):
        for arg in expr.args:
            points, warning = findCriticalPoints(arg, x)
            for i in points:
                res.append(i)    
    elif getattr(expr, 'is_Add', False): 
        for i in findSolution(expr, x):
            warning = True
            res.append(i)
        return res, warning
    else:
        points, warning = findCriticalPoints(expr, x)
        for i in points:
            res.append(i)

    return res, warning
