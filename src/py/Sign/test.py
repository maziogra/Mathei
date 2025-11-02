import sympy as sp
import test as test

def test(intervalli, segni, f, x):
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
    return segni, intervalli