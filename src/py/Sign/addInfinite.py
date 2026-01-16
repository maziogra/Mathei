import sympy as sp

def addInfinite(interlvals):
    if interlvals[0] != -sp.oo:
        ratio = interlvals[0] / sp.pi
        if not ratio.is_rational or interlvals[0] == 0:
            interlvals.insert(0, -sp.oo)
            print(interlvals)
    if interlvals[-1] != sp.oo:
        ratio = interlvals[-1] / sp.pi
        if not ratio.is_rational:
            interlvals.append(sp.oo)
            print(interlvals)