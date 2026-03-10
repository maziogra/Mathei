# Autore: Shahid
import sympy as sp

def addInfinite(intervals):
    if intervals[0] != -sp.oo:
        if not intervals[0].has(sp.pi):
            intervals.insert(0, -sp.oo)
    if intervals[-1] != sp.oo:
        if not intervals[-1].has(sp.pi):
            intervals.append(sp.oo)