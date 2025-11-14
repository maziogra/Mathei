import sympy as sp;
import Utils.trovaPeriodo as trovaPeriodo;
def intersezioni(funzione):
    x=sp.symbols("x")
    R=sp.S.Reals
    if isGoniometrica(funzione):
       R=trovaPeriodo()
    #int con asse x y=0
    intersezionixy=[]
    try:
        zeri = sp.solveset(funzione, x, R)
        if isinstance(zeri, sp.FiniteSet):
            for zero in zeri:
                intersezionixy.append((zero,0))
    except Exception as excep:
        intersezionixy.append("errore asse x")  
    #int con asse y x=0 
    try:
        perxZero=funzione.subs(x,0).evalf()
        if perxZero.is_real and perxZero.is_finite:
            intersezionixy.append((0,perxZero))
    except Exception as excep:
        intersezioni.append("errore asse y ")

    #risultati stmpa
    print("punti di intersezione con gli assi ")
    for punto in intersezionixy:
        print(punto)
    return(intersezionixy)
# controllo ha gongio
def isGoniometrica(f):
    goniometriche = [sp.sin, sp.cos, sp.tan, sp.cot, sp.sec, sp.csc]
    return any(f.has(func) for func in goniometriche)