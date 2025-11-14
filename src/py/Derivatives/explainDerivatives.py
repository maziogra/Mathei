import sympy as sp

def explainDerivatives(f, x):
    print(f"Funzione considerata: f(x) = {f}\n")
    if isinstance(f, sp.Add):
        print("Regola applicata: Somma")
        termini = []
        for termine in f.args:
            print(f"Termine: {termine}")
            d_termine = explainDerivatives(termine, x)
            termini.append(d_termine)
        derivative = sum(termini)

    elif isinstance(f, sp.Mul) and any(isinstance(arg, sp.Pow) and arg.exp == -1 for arg in f.args):
        num = sp.Mul(*[arg for arg in f.args if not (isinstance(arg, sp.Pow) and arg.exp == -1)])
        den = [arg.base for arg in f.args if isinstance(arg, sp.Pow) and arg.exp == -1][0]
        u = num
        v = den
        du = sp.diff(u, x)
        dv = sp.diff(v, x)
        print("Regola applicata: derivata del quoziente")
        print(f"  f(x) = {u} / {v}")
        print(f"  f'(x) = ({du}) * ({v}) - ({u}) * ({dv}) / ({v})**2")
        derivative = sp.diff(f, x)

    elif isinstance(f, sp.Mul):
        print("Regola applicata: derivata del prodotto")
        fattori = f.args
        n = len(fattori)

        termini_derivati = []
        for i in range(n):
            du_i = sp.diff(fattori[i], x)
            altri_fattori = [fattori[j] for j in range(n) if j != i]
            prodotto_altri = sp.Mul(*altri_fattori)
            termine = du_i * prodotto_altri
            print(f"  Derivata del fattore {i+1}: d({fattori[i]})/dx = {du_i}")
            print(f"    → Termine: {du_i} * {' * '.join(str(f) for f in altri_fattori)} = {termine}")
            termini_derivati.append(termine)
        derivative = sum(termini_derivati)

    elif isinstance(f, sp.Function):
        inner = f.args[0]
        outer = f.func
        outer_func_applied = type(f)(inner)
        d_outer = sp.diff(outer_func_applied, x)
        d_inner = sp.diff(inner, x)
        print("Regola applicata: derivata di funzione composta (regola della catena)")
        print(f"  f(x) = {outer.__name__}({inner})")
        print(f"  Derivata esterna rispetto all'interno: d/d({inner}) {outer.__name__} = {d_outer}")
        print(f"  Derivata interna: d({inner})/dx = {d_inner}")
        print(f"  f'(x) = {d_outer} * {d_inner}")
        derivative = sp.diff(f, x)
    
    else:
        print("Calcolo derivata generica (nessuna regola specifica rilevata)")
        derivative = sp.diff(f, x)
        print(f"  Derivata = {derivative}")

    #derivata_simplificata = sp.simplify(derivata)
    return derivative
