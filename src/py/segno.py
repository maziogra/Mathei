import sympy as sp;
from trovaPeriodo import trovaPeriodo;

def segno(f, x):
    
    # trovo zeri e dominio da cui estrarro i punti critici
    punti = sp.solveset(f, x, domain=sp.S.Reals);
    dominio = sp.calculus.util.continuous_domain(f, x, sp.S.Reals);
    gonio = False;
    
    # se i punti sono finiti vuoldire che non è una goniometrica
    # da rivedere, forse ci sono altri casi
    if isinstance(punti, sp.FiniteSet):
        punti = list(punti);
    else:
        # funzione per trovare il periodo
        per = trovaPeriodo(f,x)
        gonio = True;
        if per is not None:
            # periodo trovato
            punti = list(sp.solveset(f, x, domain=sp.Interval(0, per)))
            dominio = sp.calculus.util.continuous_domain(f, x, sp.Interval(0, per));
        else:
            # limitazione disperata del periodo (anche se non c'è)
            punti = list(sp.solveset(f, x, domain=sp.Interval(-10, 10)));
            dominio = sp.calculus.util.continuous_domain(f, x, domain=sp.Interval(-10, 10));
    
    # metto nell'insieme dei punti anche i punti in cui la funz non esiste
    if isinstance(dominio, sp.Union):
        for intervallo in dominio.args:
            for limite in [intervallo.start, intervallo.end]:
                if limite in punti:
                    continue;
                if limite != sp.oo and limite != -sp.oo:
                    punti.append(limite);
    if isinstance(dominio, sp.Interval):
        for limite in [dominio.start, dominio.end]:
            if limite in punti:
                    continue;
            if limite != sp.oo and limite != -sp.oo:
                punti.append(limite);
                
    # ritorno -1 se non ci sono punti in cui la funzione cambia segno
    if(punti == []):
        return -1;
        
    punti = sorted(punti);
    
    # aggiungo agli estremi gli infiniti per considerare tutti gli intervalli sensati
    intervalli = [-sp.oo] + punti + [sp.oo];
    
    segni = [];


    #controllo il segno in ogni intervallo facendo attenzione agli infiniti
    for i in range(len(intervalli)-1):
        a = intervalli[i];
        b = intervalli[i+1];
        
        if a == -sp.oo and b != sp.oo:
            test = b - 1;
        elif b == sp.oo and a != -sp.oo:
            test = a + 1;
        elif a != -sp.oo and b != sp.oo:
            test = (a + b) / 2
        else:
            test = 0;

        try:
            valore = f.subs(x, test).evalf();
            if valore > 0:
                segni.append('+');
            elif valore < 0:
                segni.append('-');
            else:
                segni.append('0');
        except:
            segni.append("non definito");
            
    # se è goniometrica tolgo gli intervalli agli estremi, altrimenti mi direbbe una cosa sbagliata
    # direbbe che all'infinito la funzione ha sempre lo stesso segno, ma non è vero dato che stiamo considerando
    # solo un intervallo limitato 
    if gonio:
        intervalli.pop(0);
        intervalli.pop();
        segni.pop(0);
        segni.pop();
        
    # Stampa dei risultati provvisoria, poi da rimuovere, tanto serve solo per debug
    for i in range(len(segni)):
        print(f"Intervallo {intervalli[i]} -> {intervalli[i+1]}: segno {segni[i]}")

    return punti, segni;