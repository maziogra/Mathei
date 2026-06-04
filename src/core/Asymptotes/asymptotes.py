# Autore: Khadija

import sympy as sp
from core.Limits.limits import limits
from core.Domain.domain import domain
from core.Utils.findPeriod import findPeriod     
from core.Utils.isGonio import isGonio

def asymptotes(f, x):
    dominio, warning = domain(f, x)
    if warning == None:
        warning = False
    else:
        warning = True
    risultati = {}

  #orzzontali
    asintoti_orizzontali = []

    try:
        limite_inf_pos = limits(f, x, sp.oo)
        if limite_inf_pos.is_real and limite_inf_pos.is_finite:
            asintoti_orizzontali.append(limite_inf_pos)
    except Exception:
        pass

    try:
        limite_inf_neg = limits(f, x, -sp.oo)
        if limite_inf_neg.is_real and limite_inf_neg.is_finite and limite_inf_neg not in asintoti_orizzontali:
            asintoti_orizzontali.append(limite_inf_neg)
    except Exception:
        pass

    risultati["asintoti orizzontali"] = asintoti_orizzontali
    
    #obliqui
    asintoti_obliqui = []

    try:
        if limits(f, x, sp.oo) not in asintoti_orizzontali:

            m_pos = limits(f / x, x, sp.oo)

            if m_pos.is_real and m_pos != 0 and m_pos.is_finite:

                q_pos = limits(f - m_pos * x, x, sp.oo)

                if q_pos.is_finite:
                    asintoti_obliqui.append([
                        float(m_pos),
                        float(q_pos)
                    ])

    except Exception:
        pass


    try:
        if limits(f, x, -sp.oo) not in asintoti_orizzontali:

            m_neg = limits(f / x, x, -sp.oo)

            if m_neg.is_real and m_neg != 0 and m_neg.is_finite:

                q_neg = limits(f - m_neg * x, x, -sp.oo)

                if q_neg.is_finite:

                    asint = [
                        float(m_neg),
                        float(q_neg)
                    ]

                    if asint not in asintoti_obliqui:
                        asintoti_obliqui.append(asint)

    except Exception:
        pass
        
        
    risultati["asintoti obliqui"] = asintoti_obliqui   # (m,q),(m1,q1)...

    #possibili verticali caso; x-1/(x**2-1)
    punti_da_analizzare = []

    if isGonio(f, x):
        period = findPeriod(f, x)
        if not period:
            return [], True
        try:
            dominio = sp.calculus.util.continuous_domain(f, x, domain=sp.Interval(-period, period, left_open=False, right_open=False)) 
        except Exception:
            return [], True

    if isinstance(dominio, sp.Union):
        for intervallo in dominio.args:
            if hasattr(intervallo, 'left_open') and intervallo.left_open:
                punti_da_analizzare.append(intervallo.start)
            if hasattr(intervallo, 'right_open') and intervallo.right_open:
                punti_da_analizzare.append(intervallo.end)
    elif isinstance(dominio, sp.Interval):
        if dominio.left_open:
            punti_da_analizzare.append(dominio.start)
        if dominio.right_open:
            punti_da_analizzare.append(dominio.end)

    punti_da_analizzare = sorted(
        {p for p in punti_da_analizzare if p != sp.oo and p != -sp.oo}
    )

    #veriticlai ediscontinuita
    asintoti_verticali = []
    f = sp.expand_trig(f)
    for punto in punti_da_analizzare:
        try:
            lim_sx = limits(f, x, punto, '-')
            lim_dx = limits(f, x, punto, '+')


            if lim_sx == lim_dx and lim_sx.is_real:
                continue
            elif abs(lim_sx) == sp.oo or abs(lim_dx) == sp.oo:
                asintoti_verticali.append(punto)
            

        except Exception:
            asintoti_verticali.append(punto)

    risultati["asintoti verticali"] = asintoti_verticali

    return risultati, warning
