import sympy as sp


def isGonio(f, x):
     return any(
        trig.has(x)
        for trig in (sp.sin, sp.cos, sp.tan)
        if f.has(trig))