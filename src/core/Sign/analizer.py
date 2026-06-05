# Autore: Shahid

import sympy as sp
from core.Sign.findCriticalPoints import findCriticalPoints
from core.Sign.findSolution import findSolution

def analizer(expr, x):
    res = []
    warning = False
    tag = False

    if expr.is_polynomial(x):
        points, warning = findCriticalPoints(expr, x)
        for i in points:
            res.append(i)
        return res, warning
    
    # Mul, Add ecc. con i metodi di sympy
    if getattr(expr, 'is_Mul', False):
        for arg in expr.args:
            points, warning = findCriticalPoints(arg, x)
            if isinstance(points, sp.ConditionSet) or points.has(sp.ConditionSet):
                tag = True
            else:
                for i in points:
                    res.append(i)    
    else:
        points, warning = findCriticalPoints(expr, x)
        if isinstance(points, sp.ConditionSet) or points.has(sp.ConditionSet):
            tag = True
        else:
            for i in points:
                res.append(i)

    if tag: 
        for i in findSolution(expr, x):
            warning = True
            res.append(i)
        return res, warning

    return list(set(res)), warning
