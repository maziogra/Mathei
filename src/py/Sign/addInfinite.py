# Autore: Shahid

import sympy as sp

def addInfinite(intervals):
    if intervals[0] != -sp.oo:
        if intervals[0].has("pi"):
            intervals.insert(0, -sp.oo)
    if intervals[-1] != sp.oo:
        if intervals[-1].has("pi"):
            intervals.append(sp.oo)