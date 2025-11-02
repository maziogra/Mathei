import sympy as sp
x = sp.symbols('x', real=True)
f = sp.log(x)*sp.cos(x + 3) + sp.sin(x)


def findSoluntion(f, x):
    a = float(0)
    b = float(2 * sp.pi)

    guesses = [a + i*(b-a)/50 for i in range(1,50)]
    solutions = set()
    for g in guesses:
        try:
            r = sp.nsolve(f, g, tol=1e-14, maxsteps=50)
            rv = float(r)
            if a <= rv <= b:
                solutions.add(round(rv, 12))
        except Exception:
            pass

    solutions = sorted(solutions)
    return solutions