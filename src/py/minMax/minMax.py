import sympy as sp
from Sign.createSign import createSign 
from Domain.domain import domain

def minMax(f, x):
    f1 = sp.diff(f, x)
    f1 = sp.simplify(f1)
    intervals, signs = createSign(f1, x)

    if(len(signs) == 1):
        return []
    
    try:
        intervals.remove(-sp.oo)
        intervals.remove(sp.oo)
    except:
        print("Nessun infinito rimosso")
    
    d = domain(f, x)

    if intervals[0] in d or f.subs(x, intervals[0]).evalf() != 0:
        intervals.pop(0)

    if intervals[-1] in d or f.subs(x, intervals[-1]).evalf() != 0:
        intervals.pop(-1)

    print("-----------", intervals[0] in d)

    k = 0
    punti = []
    sign_p = ""

    for i in signs:
        if k == 0:
            sign_p = i
        elif sign_p == "+" and i == "-":
            punti.append((intervals[k-1], "max"))
        elif sign_p == "-" and i == "+":
            punti.append((intervals[k-1], "min"))
        sign_p = i
        k += 1

    punti = [i for i in punti if i[0] in d]
    print(punti)