# Autore: Shahid
import sympy as sp

def addInfinite(intervals):
    
    if len(intervals) == 0:
        intervals.insert(0, -sp.oo)
        intervals.append(sp.oo)
    if intervals[0] != -sp.oo:
        intervals.insert(0, -sp.oo)
    if intervals[-1] != sp.oo:
        intervals.append(sp.oo)
