# Autore: maziogra
# Refactoring: Shahid

import sympy as sp

def test(intervals, sign, f, x):
    for i in range(len(intervals) - 1):
        a = intervals[i]
        b = intervals[i + 1]
        
        if a == -sp.oo and b != sp.oo:
            test = b - 1
        elif b == sp.oo and a != -sp.oo:
            test = a + 1
        elif a != -sp.oo and b != sp.oo:
            test = (a + b) / 2
        else:
            test = 0

        try:
            valore = f.subs(x, test).evalf()
            if valore > 0:
                sign.append('+')
            elif valore < 0:
                sign.append('-')
            else:
                sign.append('0')
        except:
            sign.append("non definito")
    return sign, intervals