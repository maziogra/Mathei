# Autore: Shahid
# Refactoring TOTALE: tutti

from core.Sign.addInfinite import addInfinite
from core.Sign.test import test
from core.Sign.analizer import analizer
import sympy as sp

def createSign(f, x):
    intervals, warning = analizer(f, x)
    
    intervals = [i for i in set(intervals) if intervals.count(i) >= 1]
    intervals = sorted(intervals)
    
    
    intervals = [sp.sympify(i) for i in intervals]
    
    f_exp = sp.expand_trig(f)
    if not f_exp.has(sp.cos, sp.sin, sp.tan):
        addInfinite(intervals)
    
    print("Final intervals:")
    print(intervals)

    signs = test(intervals, f, x)
    print("Signs: ")
    print(signs)

    return intervals, signs, warning
