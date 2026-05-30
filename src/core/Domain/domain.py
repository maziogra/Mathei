# Autore: Khadija

import sympy as sp
from core.Utils.findPeriod import findPeriod

def domain(f, x):
    k = sp.symbols('k', integer=True)
    dom = sp.S.Reals

    for underExp in sp.preorder_traversal(f):

        # --- Denominatore ---
        function_simplified = sp.together(underExp)
        den = sp.denom(function_simplified)

        if den != 1:
            try:
                zero_den = sp.solveset(sp.Eq(den, 0), x, sp.S.Reals)
                if zero_den != sp.EmptySet:
                    dom = dom - zero_den
            except Exception:
                pass

        # --- Potenze / radici ---
        if isinstance(underExp, sp.Pow):
            base = underExp.args[0]
            exp  = underExp.args[1]

            if exp.is_Rational and exp.q % 2 == 0 and exp.p > 0:
                # radice pari con esponente positivo: base >= 0
                try:
                    cond = sp.solveset(sp.Ge(base, 0), x, sp.S.Reals)
                    dom = dom.intersect(cond)
                except Exception:
                    pass

            elif exp.is_Rational and exp.q % 2 == 0 and exp.p < 0:
                # radice pari con esponente negativo: base > 0
                try:
                    cond = sp.solveset(sp.Gt(base, 0), x, sp.S.Reals)
                    dom = dom.intersect(cond)
                except Exception:
                    pass

            elif not exp.is_Rational or exp.has(x):
                # esponente irrazionale (x^x ecc.): base > 0
                try:
                    cond = sp.solveset(sp.Gt(base, 0), x, sp.S.Reals)
                    dom = dom.intersect(cond)
                except Exception:
                    pass

        # --- Logaritmo ---
        elif isinstance(underExp, sp.log):
            arg = underExp.args[0]
            try:
                cond = sp.solveset(sp.Gt(arg, 0), x, sp.S.Reals)
                dom = dom.intersect(cond)
            except Exception:
                pass

        # --- tan, sec  →  escludi arg = π/2 + kπ ---
        elif underExp.func in (sp.tan, sp.sec):
            arg = underExp.args[0]
            try:
                sol = sp.solveset(sp.Eq(arg, sp.pi / 2), x, domain=sp.S.Reals)
                if sol != sp.EmptySet:
                    period = findPeriod(underExp, x)
                    if period is not None and sol.is_FiniteSet:
                        base_pt = list(sol)[0]
                        cond = sp.ImageSet(sp.Lambda(k, base_pt + k * period), sp.S.Integers)
                        dom = dom - cond
                    elif sol.is_FiniteSet:
                        dom = dom - sol
            except Exception:
                pass

        # --- cot, csc  →  escludi arg = kπ ---
        elif underExp.func in (sp.cot, sp.csc):
            arg = underExp.args[0]
            try:
                sol = sp.solveset(sp.Eq(arg, 0), x, domain=sp.S.Reals)
                if sol != sp.EmptySet:
                    period = findPeriod(underExp, x)
                    if period is not None and sol.is_FiniteSet:
                        base_pt = list(sol)[0]
                        cond = sp.ImageSet(sp.Lambda(k, base_pt + k * period), sp.S.Integers)
                        dom = dom - cond
                    elif sol.is_FiniteSet:
                        dom = dom - sol
            except Exception:
                pass

        elif underExp.func in (sp.asin, sp.acos):
            arg = underExp.args[0]
            try:
                cond_lower = sp.solveset(sp.Ge(arg, -1), x, domain=sp.S.Reals)
                cond_upper = sp.solveset(sp.Le(arg,  1), x, domain=sp.S.Reals)
                dom = dom.intersect(cond_lower).intersect(cond_upper)
            except Exception:
                pass

    print("dominio:", dom)
    return dom