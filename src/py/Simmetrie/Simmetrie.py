import sympy as sp
def simmetrie(funzione):
    x = sp.symbols('x')
    f_piux=funzione
    f_menox = funzione.subs(x, -x)
    if sp.simplify(f_piux - f_menox) == 0:
        return "funzioe pari, simmetrica rispetto all'asse x"
    elif sp.simplify(f_menox + f_piux) == 0:
        return " funzione dispari, simmetrica rispetto all'origine"
    else:
        return "non presenta simmetrie evidenti"