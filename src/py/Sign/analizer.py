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
            arg = sp.expand_trig(arg)
            if arg.has(sp.sin, sp.cos, sp.tan):
                for i in findNearestPeriod(arg, x):
                    res.append(i)    
            else:
                for i in findCriticalPoints(arg, x):
                    res.append(i)
    elif getattr(expr, 'is_Add', False): 
        for i in findSolution(expr, x):
            print("Nel add: ", i)
            res.append(i)
        return res
    else:
        expr = sp.expand_trig(expr)
        if expr.has(sp.sin, sp.cos, sp.tan):
            for i in findNearestPeriod(expr, x):
                res.append(i)
        else:
            for i in findCriticalPoints(expr, x, flag):
                res.append(i)
    return res
