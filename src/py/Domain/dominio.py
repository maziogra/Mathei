import sympy as sp

def dominio(funzione):
    x = sp.symbols('x', real=True) # real=True importante se non non lo da come rational
    k = sp.symbols('k', integer=True)
    #d=R
    dom = sp.S.Reals
    
    #dinom
    funzione_semplificata = sp.together(funzione)
    denominatore = sp.denom(funzione_semplificata)
    
    if denominatore != 1:
        try:
            zeri_denom = sp.solveset(sp.Eq(denominatore, 0), x, sp.S.Reals)
            if zeri_denom != sp.EmptySet:
                dom = dom - zeri_denom
        except:
            pass
    
    #funz nodo per nod
    for sottoespressione in sp.preorder_traversal(funzione):
        
        # esponenziali 
        if isinstance(sottoespressione, sp.Pow):
            base = sottoespressione.args[0]
            esponente = sottoespressione.args[1]

            if esponente.is_Rational and esponente.q % 2 == 0 and esponente.p > 0: 
                try:
                    cond = sp.solveset(sp.Ge(base, 0), x, dom)
                    dom = dom.intersect(cond)
                except:
                    pass

            elif esponente.is_Rational and esponente.q % 2 == 0 and esponente.p < 0:
                try:
                    cond = sp.solveset(sp.Gt(base, 0), x, dom) 
                    dom = dom.intersect(cond)
                except:
                    pass
            
            # esp irrazionale x^x
            elif not esponente.is_Rational or esponente.has(x):
                try:
                    cond = sp.solveset(sp.Gt(base, 0), x, dom)
                    dom = dom.intersect(cond)
                except:
                    pass
        
        #log
        elif isinstance(sottoespressione, sp.log):
            argomento = sottoespressione.args[0]
            try:
                cond = sp.solveset(sp.Gt(argomento, 0), x, dom)
                dom = dom.intersect(cond)
            except:
                pass
        
        #tan, sec p/2
        elif sottoespressione.func in (sp.tan, sp.sec):
            arg = sottoespressione.args[0]
            try:
                #periodo
                coeff = arg.coeff(x) if arg.coeff(x) else 1
                periodo = abs(coeff) if coeff != 0 else 1
                
                if periodo == 1:
                    esclusi = sp.ImageSet(sp.Lambda(k, sp.pi/2 + k*sp.pi), sp.S.Integers)
                else:
                    esclusi = sp.ImageSet(sp.Lambda(k, sp.pi/(2*periodo) + k*sp.pi/periodo), sp.S.Integers)
                
                dom = dom - esclusi
            except:
                pass
        
        # cotn,cosc kp
        elif sottoespressione.func in (sp.cot, sp.csc):
            arg = sottoespressione.args[0]
            try:
                coeff = arg.coeff(x) if arg.coeff(x) else 1
                periodo = abs(coeff) if coeff != 0 else 1
                
                if periodo == 1:
                    esclusi = sp.ImageSet(sp.Lambda(k, k*sp.pi), sp.S.Integers)
                else:
                    esclusi = sp.ImageSet(sp.Lambda(k, k*sp.pi/periodo), sp.S.Integers)
                
                dom = dom - esclusi
            except:
                pass
        
        # arcos, arcsen -1,1
        elif sottoespressione.func in (sp.asin, sp.acos):
            arg = sottoespressione.args[0]
            try:
                cond = sp.solveset(sp.And(arg >= -1, arg <= 1), x, dom)
                dom = dom.intersect(cond)
            except:
                pass
        
    
    print("dominio:", dom)
    return dom



