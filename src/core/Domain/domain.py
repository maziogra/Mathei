import sympy as sp
from core.Utils.findPeriod import findPeriod


def domain(f, x):
    k = sp.symbols('k', integer=True)
    dom = sp.S.Reals

    for underExp in sp.preorder_traversal(f):

        function_simplified = sp.together(underExp)
        den = sp.denom(function_simplified)

        if den != 1:
            try:
                zero_den = sp.solveset(sp.Eq(den, 0), x, sp.S.Reals)

                if isinstance(zero_den, sp.ConditionSet):
                    return None, f"Denominatore non risolvibile: {den}"

                dom = dom - zero_den

            except Exception:
                return None, f"Errore nel denominatore: {den}"

        if isinstance(underExp, sp.Pow):
            base, exp = underExp.args

            # radice pari
            if exp.is_Rational and exp.q % 2 == 0:

                # base complessa (heuristic)
                if base.has(sp.sin, sp.cos, sp.tan, sp.exp, sp.log):
                    return None, f"Radice pari con espressione complessa: {base}"

                try:
                    cond = sp.solveset(sp.Ge(base, 0), x, sp.S.Reals)

                    if isinstance(cond, sp.ConditionSet):
                        return None, f"Condizione non risolvibile per radice: {base}"

                    dom = dom.intersect(cond)

                except Exception:
                    return None, f"Errore nella radice: {base}"

            # esponente irrazionale
            elif not exp.is_Rational or exp.has(x):
                try:
                    cond = sp.solveset(sp.Gt(base, 0), x, sp.S.Reals)
                    dom = dom.intersect(cond)
                except Exception:
                    return None, f"Errore esponente irrazionale: {base}"

        elif isinstance(underExp, sp.log):
            arg = underExp.args[0]

            try:
                cond = sp.solveset(sp.Gt(arg, 0), x, sp.S.Reals)

                if isinstance(cond, sp.ConditionSet):
                    return None, f"Log non risolvibile: {arg}"

                dom = dom.intersect(cond)

            except Exception:
                return None, f"Errore logaritmo: {arg}"

        elif underExp.func in (sp.tan, sp.sec):
            arg = underExp.args[0]

            try:
                sol = sp.solveset(sp.Eq(arg, sp.pi / 2), x, domain=sp.S.Reals)

                if sol != sp.EmptySet:
                    period = findPeriod(underExp, x)

                    if period is None:
                        return None, f"Periodo non trovato per: {underExp}"

                    if sol.is_FiniteSet:
                        base_pt = list(sol)[0]
                        cond = sp.ImageSet(
                            sp.Lambda(k, base_pt + k * period),
                            sp.S.Integers
                        )
                        dom = dom - cond

            except Exception:
                return None, f"Errore trigonometrico: {underExp}"

        elif underExp.func in (sp.cot, sp.csc):
            arg = underExp.args[0]

            try:
                sol = sp.solveset(sp.Eq(arg, 0), x, sp.S.Reals)

                if sol != sp.EmptySet:
                    period = findPeriod(underExp, x)

                    if period is None:
                        return None, f"Periodo non trovato: {underExp}"

                    if sol.is_FiniteSet:
                        base_pt = list(sol)[0]
                        cond = sp.ImageSet(
                            sp.Lambda(k, base_pt + k * period),
                            sp.S.Integers
                        )
                        dom = dom - cond

            except Exception:
                return None, f"Errore cot/csc: {underExp}"

        elif underExp.func in (sp.asin, sp.acos):
            arg = underExp.args[0]

            try:
                cond1 = sp.solveset(sp.Ge(arg, -1), x, sp.S.Reals)
                cond2 = sp.solveset(sp.Le(arg, 1), x, sp.S.Reals)

                if isinstance(cond1, sp.ConditionSet) or isinstance(cond2, sp.ConditionSet):
                    return None, f"Dominio asin/acos non risolvibile: {arg}"

                dom = dom.intersect(cond1).intersect(cond2)

            except Exception:
                return None, f"Errore asin/acos: {arg}"

    return dom, None