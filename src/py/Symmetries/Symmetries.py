# Autore: Khadija

import sympy as sp
def symmetries(f):
    x = sp.symbols('x')
    f_plusx=f
    f_minusx = f.subs(x, -x)
    if sp.simplify(f_plusx - f_minusx) == 0:
        return "funzioe pari, simmetrica rispetto all'asse x"
    elif sp.simplify(f_minusx + f_plusx) == 0:
        return " funzione dispari, simmetrica rispetto all'origine"
    else:
        return "non presenta simmetrie evidenti"