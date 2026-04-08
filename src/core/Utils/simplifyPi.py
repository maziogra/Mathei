import sympy as sp

def simplifyPi(x, tol=1e-6):
    x = float(x)
    k = round(x / (float(sp.pi)/2))
    candidate = k * sp.pi / 2
    if abs(x - float(candidate)) < tol:
        return sp.simplify(candidate)
    return x