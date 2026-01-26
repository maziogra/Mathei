# Autore: Shahid

import sympy as sp

def addInfinite(intervals):
    if intervals[0] != -sp.oo:
        ratio = intervals[0] / sp.pi
        if not ratio.is_rational or intervals[0] == 0:
            intervals.insert(0, -sp.oo)
            print(intervals)
    if intervals[-1] != sp.oo:
        ratio = intervals[-1] / sp.pi
        if not ratio.is_rational:
            intervals.append(sp.oo)
            print(intervals)