import sympy as sp;

def trovaPeriodo(f, x):
    f = sp.expand_trig(f)
    periodi = []
    
    for n in f.atoms(sp.sin, sp.cos, sp.tan):
        arg = n.args[0]
        coeff = arg.coeff(x)

        if coeff == 0:
            continue

        periodo = None
        if isinstance(n, sp.sin) or isinstance(n, sp.cos):
            periodo = 2*sp.pi / abs(coeff)
        elif isinstance(n, sp.tan):
            periodo = sp.pi / abs(coeff)
        
        if periodo is not None:
            periodi.append(periodo)
            
    if not periodi:
        return None
    
    periodi_pi = []
    
    for p in periodi:
        periodi_pi.append(p / sp.pi)
    
    mcm = sp.lcm_list(periodi_pi) * sp.pi

    return sp.simplify(mcm)