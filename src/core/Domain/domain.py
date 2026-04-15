# Autore: Khadija

import sympy as sp
from core.Utils.findPeriod import findPeriod

def domain(f, x):
    k = sp.symbols('k', integer=True)
    #d=R
    dom = sp.S.Reals
    
    #funz nodo per nod
    for underExp in sp.preorder_traversal(f):

        function_simplified = sp.together(underExp)
        den = sp.denom(function_simplified)
        
        if den != 1:
            try:
                zero_den = sp.solveset(sp.Eq(den, 0), x, sp.S.Reals)
                print(den, "###############", zero_den)
                if zero_den != sp.EmptySet:
                    dom = dom - zero_den
            except:
                pass

        # esponenziali 
        if isinstance(underExp, sp.Pow):
            base = underExp.args[0]
            exp = underExp.args[1]

            if exp.is_Rational and exp.q % 2 == 0 and exp.p > 0:
                try:
                    cond = sp.solveset(sp.Ge(base, 0), x, dom)
                    dom = dom.intersect(cond)
                except:
                    pass

            elif exp.is_Rational and exp.q % 2 == 0 and exp.p < 0:
                try:
                    cond = sp.solveset(sp.Gt(base, 0), x, dom) 
                    dom = dom.intersect(cond)
                except:
                    pass
            
            # esp irrazionale x^x
            elif not exp.is_Rational or exp.has(x):
                try:
                    cond = sp.solveset(sp.Gt(base, 0), x, dom)
                    dom = dom.intersect(cond)
                except:
                    pass
        
        #log
        elif isinstance(underExp, sp.log):
            argomento = underExp.args[0]
            try:
                cond = sp.solveset(sp.Gt(argomento, 0), x, dom)
                dom = dom.intersect(cond)
            except:
                pass

        #tan, sec p/2 
        elif underExp.func in (sp.tan, sp.sec):
            arg = underExp.args[0]
            try:
                for punti in [sp.pi/2, 3*sp.pi/2]:
                    sol = sp.solveset(sp.Eq(arg, punti), x, domain=dom)
                    if sol != sp.EmptySet and sol.is_FiniteSet:
                        base = list(sol)[0]  # se è piriodica basta la piram sol
                        
                        period = findPeriod(underExp, x)
                        print("----------------", period)
                        if period is not None:
                            cond = sp.ImageSet(sp.Lambda(k, base + k*period), sp.S.Integers)
                            dom = dom - cond
                            break
                        else:
                            dom = dom - sol   
            except:
                pass
        
        # cotn,cosc kp
        elif underExp.func in (sp.cot, sp.csc):
            arg = underExp.args[0]
            try:
                for punti in [sp.pi, 2*sp.pi]:
                    sol = sp.solveset(sp.Eq(arg, punti), x, domain=dom)
                    if sol != sp.EmptySet and sol.is_FiniteSet:
                        base = list(sol)[0]  # se è piriodica basta la piram sol
                        
                        period = findPeriod(underExp, x)
                        if period is not None:
                            cond = sp.ImageSet(sp.Lambda(k, base + k*period), sp.S.Integers)
                            dom = dom - cond
                            break
                        else:
                            dom = dom - sol   
            except:
                pass
        
        # arcos, arcsen -1,1
        elif underExp.func in (sp.asin, sp.acos):
            arg = underExp.args[0]
            try:
                cond = sp.solveset(sp.And(arg >= -1, arg <= 1), x, dom)
                dom = dom.intersect(cond)
            except:
                pass
                
        
    
    print("dominio:", dom)
    return dom