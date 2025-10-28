import sympy as sp;
from trovaPeriodo import trovaPeriodo;

def trovaPuntiCritici(f, x):
    # trovo zeri e dominio da cui estrarro i punti critici
    punti = sp.solveset(f, x, domain=sp.S.Reals);
    dominio = sp.calculus.util.continuous_domain(f, x, sp.S.Reals);
    gonio = False;
    
    # se i punti sono finiti vuoldire che non è una goniometrica
    # da rivedere, forse ci sono altri casi
    if isinstance(punti, sp.FiniteSet) or punti == sp.EmptySet:
        punti = list(punti);
    else:
        # funzione per trovare il periodo
        per = trovaPeriodo(f,x)
        gonio = True;
        if per is not None:
            # periodo trovato
            punti = sp.solveset(f, x, domain=sp.Interval(0, per));
            if isinstance(punti, sp.FiniteSet):
                punti = list(sp.solveset(f, x, domain=sp.Interval(0, per)))
                dominio = sp.calculus.util.continuous_domain(f, x, sp.Interval(0, per));
            else:
                punti = [];
                # questo lo metto a false altrimenti nella funzione segno toglie il primo e l'ultimo intervallo che creo
                # per poter effettuare i test, che in questo caso non riesce a generare in quanto non c'è nemmeno un punto intermedio a cui appoggiarsi
                gonio = False;
                return punti, gonio, False;
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
    
    return punti, gonio, True;
    
