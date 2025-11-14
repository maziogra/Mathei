import sympy as sp
from Sign.findNearestPeriod import findNearestPeriod
from Sign.trovaPuntiCritici import trovaPuntiCritici

def analizer(expr, x):
    res = []
    # Mul, Add ecc. con i metodi di sympy
    if getattr(expr, 'is_Mul', False):
        for arg in expr.args:
            if arg.has(sp.sin, sp.cos, sp.tan):
                res.append(findNearestPeriod(arg, x, []))
            else:
                res.append(trovaPuntiCritici(arg, x))
    elif getattr(expr, 'is_Add', False):
        for arg in expr.args:
            res += analizer(arg, x)
    else:
        if expr.has(sp.sin, sp.cos, sp.tan):
            res.append(findNearestPeriod(expr, x, []))
        else:
            res.append(trovaPuntiCritici(expr, x))
    return res
