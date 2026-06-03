# Autore: maziogra

import sympy as sp

def visit(expr):
    yield expr
    for arg in expr.args:
        yield from visit(arg)

def notableLimits(expr, x):

    if expr == sp.sin(x)/x:
        print("Limite notevole: sin(x)/x → 1")

    elif expr == (1 - sp.cos(x))/x**2:
        print("Limite notevole: (1 - cos(x))/x^2 → 1/2")

    elif expr == (sp.exp(x) - 1)/x:
        print("Limite notevole: (e^x - 1)/x → 1")

    elif expr == sp.log(1 + x)/x:
        print("Limite notevole: ln(1+x)/x → 1")

    elif expr == (1 + x)**(1/x):
        print("Limite notevole: (1+x)^(1/x) → e")

def limits(f, x, x0, dir="+"):
    result = sp.limit(f, x, x0, dir)
    if isinstance(result, sp.AccumBounds):
        return None
    for expr in visit(f):
        if isinstance(expr, sp.Pow):
            base, exp = expr.args
            lb = sp.limit(base, x, x0, dir)
            le = sp.limit(exp, x, x0, dir)

            if lb == 1 and abs(le) == sp.oo:
                print("Forma indeterminata 1^∞ in", expr)
            elif lb == 0 and le == 0:
                print("Forma indeterminata 0^0 in", expr)
            elif abs(lb) == sp.oo and le == 0:
                print("Forma indeterminata ∞^0 in", expr)
            continue

        if expr.is_Rational is False and sp.denom(expr) != 1:
            num, den = sp.fraction(expr)
            ln = sp.limit(num, x, x0, dir)
            ld = sp.limit(den, x, x0, dir)

            if ln == 0 and ld == 0:
                print("Forma indeterminata 0/0 in", expr)
            elif abs(ln) == sp.oo and abs(ld) == sp.oo:
                print("Forma indeterminata ∞/∞ in", expr)
            continue

        if isinstance(expr, sp.Mul):
            lims = [sp.limit(a, x, x0, dir) for a in expr.args]
            if 0 in lims and any(abs(l) == sp.oo for l in lims):
                print("Forma indeterminata 0·∞ in", expr)
        notableLimits(expr, x)

    return result