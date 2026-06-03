# Autore: Shahid
# Refactoring TOTALE: tutti

from core.Sign.addInfinite import addInfinite
from core.Sign.test import test
from core.Sign.analizer import analizer
from core.Utils.isGonio import isGonio

import sympy as sp

def createSign(f, x):
    intervals, warning = analizer(f, x)

    intervals = [sp.sympify(i) for i in intervals]
    intervals = [p for p in intervals if p.is_real is True]
    intervals = sorted(intervals)
    
    f_exp = sp.expand_trig(f)
    if not isGonio(f_exp, x):
        addInfinite(intervals)
    
    print("Final intervals:")
    print(intervals)

    signs = test(intervals, f, x)
    print("Signs: ")
    print(signs)

    return intervals, signs, warning
