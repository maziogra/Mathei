# Autore: maziogra

import sympy as sp

def findPeriod(f, x):
    f = sp.expand_trig(f)
    periods = []
    
    for n in f.atoms(sp.sin, sp.cos, sp.tan):
        arg = n.args[0]
        coeff = arg.coeff(x)

        if coeff == 0:
            continue

        period = None
        if isinstance(n, sp.sin) or isinstance(n, sp.cos):
            period = 2*sp.pi / abs(coeff)
        elif isinstance(n, sp.tan):
            period = sp.pi / abs(coeff)
        
        if period is not None:
            periods.append(period)
            
    if not periods:
        return None
    
    periodi_pi = []
    
    for p in periods:
        periodi_pi.append(p / sp.pi)
    
    mcm = sp.lcm_list(periodi_pi) * sp.pi

    return sp.simplify(mcm)