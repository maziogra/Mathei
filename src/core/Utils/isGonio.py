import sympy as sp


def isGonio(f, x):
    return any(
        f.has(trig) and f.has(x)
        for trig in (sp.sin, sp.cos, sp.tan, sp.cot, sp.sec, sp.csc, sp.cot, sp.acos, sp.asin, sp.atan, sp.acot)
    )