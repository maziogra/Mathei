import sympy as sp
from Sign.createSign import createSign 
from Domain.domain import domain

def minMax(f, x):
    f1 = sp.diff(f, x)
    f1 = sp.simplify(f1)
    intervals, signs, warning = createSign(f1, x)

    print(intervals)
    if(len(signs) == 1):
        return []
    
    
    d = domain(f, x)


    punti = []
    prev = ""
    curr = ""

    for i in range(1, len(signs)):
        prev = signs[i-1]
        curr = signs[i]
        if prev == "+" and curr == "-":
            punti.append((intervals[i], f.subs(x, intervals[i]).evalf(), "max"))
        elif prev == "-" and curr == "+":
            punti.append((intervals[i], f.subs(x, intervals[i]).evalf(), "min"))

    punti = [i for i in punti if d.contains(i[0])]
    return punti, warning
