import sympy as sp
import math as math

def visita(expr):
    yield expr
    for arg in expr.args:
        yield from visita(arg)

def limiti(f, x, x0):
    risultato = sp.limit(f, x, x0)
    for expr in visita(f):
        if isinstance(expr, sp.Pow):
            base, exp = expr.args
            lb = sp.limit(base, x, x0)
            le = sp.limit(exp, x, x0)

            if lb == 1 and abs(le) == sp.oo:
                print("Forma indeterminata 1^∞ in", expr)
            elif lb == 0 and le == 0:
                print("Forma indeterminata 0^0 in", expr)
            elif abs(lb) == sp.oo and le == 0:
                print("Forma indeterminata ∞^0 in", expr)
            continue

        if expr.is_Rational is False and sp.denom(expr) != 1:
            num, den = sp.fraction(expr)
            ln = sp.limit(num, x, x0)
            ld = sp.limit(den, x, x0)

            if ln == 0 and ld == 0:
                print("Forma indeterminata 0/0 in", expr)
            elif abs(ln) == sp.oo and abs(ld) == sp.oo:
                print("Forma indeterminata ∞/∞ in", expr)
            continue

        if isinstance(expr, sp.Mul):
            lims = [sp.limit(a, x, x0) for a in expr.args]
            if 0 in lims and any(abs(l) == sp.oo for l in lims):
                print("Forma indeterminata 0·∞ in", expr)

    print(risultato)
