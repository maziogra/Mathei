import sympy as sp;
from trovaPuntiCritici import trovaPuntiCritici;

def segno(f, x):
    punti, gonio, controllo = trovaPuntiCritici(f, x);
        
    punti = sorted(punti);

    intervalli = [-sp.oo] + punti + [sp.oo];
    
    if controllo == False:
        print(f"Intervallo {intervalli[0]} -> {intervalli[1]}: segno non definito");
        return intervalli, ["non definito"];
    
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
        print(f"Intervallo {intervalli[i]} -> {intervalli[i+1]}: segno {segni[i]}");

    return punti, segni;