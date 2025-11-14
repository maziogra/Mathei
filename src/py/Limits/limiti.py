import sympy as sp
import math as math

def limiti(f, x, x0):
    f = sp.simplify(f)

    for pow_expr in f.find(sp.Pow):
        check1 = False
        check2 = False

        for arg in pow_expr.args:
            res = sp.limit(arg, x, x0)

            if check1:
                if abs(res) == sp.oo or res == 0:
                    check2 = True
                    break

            if res in [1, 0, sp.oo, -sp.oo]:
                check1 = True

        if(check1 and check2):
            print("Forma indeterminata 1^oo 0^0 oo^0")

    if(sp.denom(f) != 1):
        res0 = sp.limit(sp.denom(f), x, x0)
        res1 = sp.limit(sp.numer(f), x, x0)
        if(not (math.isfinite(res0) and math.isfinite(res1))):
            print("Forma indeterminata oo/oo, raccogli per il grado massimo")
        if(res0 == 0 and res1 == 0):
            print("Forma indeterminata 0/0, scomponi")
    
    limite_fattori = [sp.limit(fattore, x, x0) for fattore in f.args]
    
    if(isinstance(f, sp.Mul)):
        check0 = False
        checkoo = False
        for i in range(len(limite_fattori)):
            if(limite_fattori[i] == 0):
                check0 = True
            if(abs(limite_fattori[i]) == sp.oo):
                checkoo = True
        if(check0 and checkoo):
            print("Forma indeterminata oo·0, razionalizza")
    elif(isinstance(f, sp.Sum)):
        check1 = check2 = False
        for i in range(len(limite_fattori)):
            if(limite_fattori[i] == sp.oo):
                check1 = True
            if(limite_fattori[i] == -sp.oo):
                check2 = True
        if(check1 and check2):
            print("Forma indeterminata + oo - oo, raccogli o razionalizza")
